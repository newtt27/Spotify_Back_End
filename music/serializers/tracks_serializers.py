import os
from rest_framework import serializers
from music.models import Album, Artist, Genre, Track
from music.serializers.albums_serializers import AlbumSerializer
from music.serializers.artist_serializers import ArtistSerializer
from music.serializers.genre_serializers import GenreSerializer

class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    artist = ArtistSerializer()
    genres = GenreSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField() # using track.image_url for image_url
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ['id', 'name', 'genres', 'artist', 'album', 'duration_ms', 'image_url', 'video_url']

    def get_album(self, obj):
        album = obj.album
        request = self.context.get('request')

        return {
            'id': album.id,
            'name': album.name,
            'image_url': request.build_absolute_uri(album.image_url.url) if album.image_url and request else None
        }

    def get_image_url(self, obj):
        if obj.image_url:
            return self.build_absolute_uri(obj.image_url.url)
        return None

    def get_video_url(self, obj):
        if obj.video_url:
            return self.build_absolute_uri(obj.video_url.url)
        return None

    def build_absolute_uri(self, relative_path):
        request = self.context.get('request')
        if request is not None and relative_path:
            return request.build_absolute_uri(relative_path)
        return relative_path
    
class TrackCreateSerializer(serializers.ModelSerializer):
    genreIds = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    artistId = serializers.IntegerField(write_only=True)
    image_url = serializers.ImageField(required=False, allow_null=True)
    video_url = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Track
        fields = ['name', 'genreIds', 'artistId', 'image_url', 'video_url']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Tên bài hát không được để trống.")
        if len(value) > 255:
            raise serializers.ValidationError("Tên bài hát không được vượt quá 255 ký tự.")
        return value

    def validate_genreIds(self, value):
        if not value:
            return []
        genres = Genre.objects.filter(id__in=value)
        if len(genres) != len(value):
            raise serializers.ValidationError("Một hoặc nhiều ID thể loại không hợp lệ.")
        return value

    def validate_artistId(self, value):
        if not Artist.objects.filter(id=value).exists():
            raise serializers.ValidationError("ID nghệ sĩ không hợp lệ.")
        return value

    def validate_image_url(self, value):
        if value:
            valid_extensions = ['.jpg', '.jpeg', '.png']
            ext = os.path.splitext(value.name)[1].lower()
            if ext not in valid_extensions:
                raise serializers.ValidationError("File ảnh phải có định dạng JPG, JPEG hoặc PNG.")
        return value

    def validate_video_url(self, value):
        if value:
            valid_extensions = ['.mp4']
            ext = os.path.splitext(value.name)[1].lower()
            if ext not in valid_extensions:
                raise serializers.ValidationError("File video phải có định dạng MP4.")
        return value

    def create(self, validated_data):
        genre_ids = validated_data.pop('genreIds', [])
        artist_id = validated_data.pop('artistId')
        image_url = validated_data.pop('image_url', None)
        video_url = validated_data.pop('video_url', None)

        # Set default values
        validated_data['duration_ms'] = 0
        validated_data['views'] = 0
        validated_data['artist'] = Artist.objects.get(id=artist_id)
        validated_data['image_url'] = image_url  # Map image_url to image_url
        validated_data['video_url'] = video_url

        # Create track
        track = Track.objects.create(**validated_data)

        # Associate genres
        if genre_ids:
            track.genres.set(Genre.objects.filter(id__in=genre_ids))

        return track