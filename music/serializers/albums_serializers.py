from rest_framework import serializers
from music.models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'image_url']


class AlbumDetailSerializer(serializers.ModelSerializer):
    tracks = serializers.SerializerMethodField()
    artist = serializers.SerializerMethodField()
    class Meta:
        model = Album
        fields = ['id', 'name', 'artist', 'image_url', 'tracks']

    def get_artist(self, obj):
        from music.serializers.artist_serializers import ArtistSerializer
        return ArtistSerializer(obj.artist).data

    def get_tracks(self, obj):
        from music.serializers.tracks_serializers import TrackSerializer
        tracks = obj.tracks.filter(album=obj)
        return TrackSerializer(tracks, many=True, context=self.context).data