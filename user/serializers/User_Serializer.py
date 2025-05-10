from rest_framework import serializers
from user.models import User
from .UserCreatedAlbum_Serializer import UserCreatedAlbumSerializer

class UserSerializer(serializers.ModelSerializer):
    albums = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'albums']

    def get_albums(self, obj):
        albums = obj.created_albums.all()
        return UserCreatedAlbumSerializer(albums, many=True, context=self.context).data

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']