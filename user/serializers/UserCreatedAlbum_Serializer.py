from rest_framework import serializers
from user.models import UserCreatedAlbum
from music.models import Album  # để truy vấn thông tin album gốc
from music.serializers.tracks_serializers import TrackSerializer
import re  # dùng để tách số từ chuỗi

class UserCreatedAlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    tracks = serializers.SerializerMethodField()

    class Meta:
        model = UserCreatedAlbum
        fields = ['album_id', 'name', 'artist', 'image', 'tracks']

    def extract_album_pk(self, album_id):
        """Hàm này lấy phần số cuối của album_id, ví dụ 'album23' -> 23"""
        match = re.search(r'\d+', album_id)
        return int(match.group()) if match else None
    
    def get_album_instance(self, album_id):
        pk = self.extract_album_pk(album_id)
        if pk is not None:
            try:
                return Album.objects.get(pk=pk)
            except Album.DoesNotExist:
                return None
        return None

    def get_artist(self, obj):
        album = self.get_album_instance(obj.album_id)
        if album and album.artist:
            return {
                'id': album.artist.id,
                'name': album.artist.name
            }
        return None

    def get_image(self, obj):
        album = self.get_album_instance(obj.album_id)
        if album and album.image_url:
            return self.build_absolute_uri(album.image_url.url)
        return None

    def get_tracks(self, obj):
        request = self.context.get('request')  # Lấy request từ context
        track_relations = obj.tracks.all()
        tracks = [rel.track for rel in track_relations]
        return TrackSerializer(tracks, many=True, context={'request': request}).data  # Truyền request vào context

    def build_absolute_uri(self, relative_path):
        request = self.context.get('request')
        if request is not None and relative_path:
            return request.build_absolute_uri(relative_path)
        return relative_path
