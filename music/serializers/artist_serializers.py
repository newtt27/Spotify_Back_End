from rest_framework import serializers
from music.models import Artist
from music.serializers.albums_serializers import AlbumSerializer
from music.serializers.genre_serializers import GenreSerializer

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


class ArtistDetailSerializer(serializers.ModelSerializer):

    genres = serializers.SerializerMethodField()
    top_songs = serializers.SerializerMethodField()
    albums = AlbumSerializer(many=True)
    
    class Meta:
        model = Artist
        fields = ['id', 'name', 'image_url', 'followers', 'genres', 'top_songs', 'albums']
    
    def get_genres(self, obj):
        return [artist_genre.genre.name for artist_genre in obj.genres.all()]
    
    def get_top_songs(self, obj):
        from music.serializers.tracks_serializers import TrackSerializer
        top_songs = obj.tracks.filter(artist=obj).order_by('-views')[:5]
        return TrackSerializer(top_songs, many=True).data
