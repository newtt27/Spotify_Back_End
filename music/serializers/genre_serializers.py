from rest_framework import serializers
from music.models import Genre

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name']