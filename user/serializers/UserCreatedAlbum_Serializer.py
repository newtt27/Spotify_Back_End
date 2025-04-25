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
        read_only_fields = ['album_id']  # Đảm bảo rằng album_id không yêu cầu từ client


    def create(self, validated_data):
        """Override the create method to ensure the album_id is generated."""
        album_id = self.context['request'].data.get('album_id', None)  # Get album_id from data
        if not album_id:
            album_id = self.generate_unique_album_id()  # If album_id is not provided, generate it
        validated_data['album_id'] = album_id  # Set the generated album_id
        return super().create(validated_data)

    def generate_unique_album_id(self):
        """Generate album_id in format 'album' + unique ID."""
        last_album = UserCreatedAlbum.objects.all().order_by('-album_id').first()
        if last_album:
            # Lấy số ID cuối cùng của album_id
            last_number = int(last_album.album_id.replace('album', ''))
            return f"album{last_number + 1}"
        return "album1"  # Nếu không có album nào, bắt đầu từ "album1"
    
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
