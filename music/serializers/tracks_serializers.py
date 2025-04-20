from rest_framework import serializers
from music.models import Track
from music.serializers.albums_serializers import AlbumSerializer
from music.serializers.artist_serializers import ArtistSerializer

class TrackSerializer(serializers.ModelSerializer):

    album = AlbumSerializer()
    artist = ArtistSerializer()

    class Meta:
        model = Track
        fields = ['id', 'name', 'artist', 'album', 'duration_ms', 'video_url']

