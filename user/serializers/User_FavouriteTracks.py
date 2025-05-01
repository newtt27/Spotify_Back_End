from rest_framework import serializers
from ..models import UserFavouriteTrack
from music.serializers.tracks_serializers import TrackSerializer

class UserFavouriteTrackSerializer(serializers.ModelSerializer):
    track = TrackSerializer()

    class Meta:
        model = UserFavouriteTrack
        fields = ['track']