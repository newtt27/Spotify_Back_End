from rest_framework import serializers
from music.models import Track
from music.serializers.albums_serializers import AlbumSerializer
from music.serializers.artist_serializers import ArtistSerializer

class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    artist = ArtistSerializer()
    preview_url = serializers.SerializerMethodField() # using picture_url for preview_url
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ['id', 'name', 'artist', 'album', 'duration_ms', 'preview_url', 'video_url']

    def get_album(self, obj):
        album = obj.album
        request = self.context.get('request')

        return {
            'id': album.id,
            'name': album.name,
            'image_url': request.build_absolute_uri(album.image_url.url) if album.image_url and request else None
        }

    def get_preview_url(self, obj):
        if obj.album and obj.album.image_url:
            return self.build_absolute_uri(obj.album.image_url.url)
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