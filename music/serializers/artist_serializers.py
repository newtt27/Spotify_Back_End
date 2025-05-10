from rest_framework import serializers
from music.models import Artist
from music.serializers.albums_serializers import AlbumSerializer
from music.serializers.genre_serializers import GenreSerializer

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'image_url', 'tracks']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image_url and request:
            return request.build_absolute_uri(obj.image_url.url)
        return None


class ArtistDetailSerializer(serializers.ModelSerializer):
    top_songs = serializers.SerializerMethodField()
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'image_url', 'followers', 'top_songs', 'albums']

    def get_top_songs(self, obj):
        from music.serializers.tracks_serializers import TrackSerializer
        top_songs = obj.tracks.filter(artist=obj).order_by('-views')[:5]
        return TrackSerializer(top_songs, many=True, context=self.context).data
