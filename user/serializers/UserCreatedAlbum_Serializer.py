from rest_framework import serializers
from user.models import UserCreatedAlbum
from music.models import Album, Artist  # để truy vấn thông tin album gốc
from music.serializers.tracks_serializers import TrackSerializer
import re  # dùng để tách số từ chuỗi

class UserCreatedAlbumSerializer(serializers.ModelSerializer):
    # artist = serializers.SerializerMethodField()
    # artist_id = serializers.IntegerField(write_only=True, required=False)
    image = serializers.ImageField(required=False, allow_null=True) # cho phép người dùng upload ảnh local (qua multipart/form-data).
    tracks = serializers.SerializerMethodField()

    class Meta:
        model = UserCreatedAlbum
        fields = ['album_id', 'name', 'image', 'tracks']
        read_only_fields = ['album_id']  # Đảm bảo rằng album_id chỉ để hiển thị (không yêu cầu từ client)

    def create(self, validated_data):
        # Tạo album_id nếu không có
        album_id = self.context['request'].data.get('album_id', None)
        if not album_id:
            album_id = self.generate_unique_album_id()
        validated_data['album_id'] = album_id
        validated_data['user'] = self.context['request'].user  # nếu cần, đảm bảo rằng bạn gán đúng người dùng

        # Tạo đối tượng UserCreatedAlbum
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
        # Lấy phần số cuối của album_id, ví dụ: 'album1' -> 1
        pk = self.extract_album_pk(album_id)
        if pk is not None:
            try:
                # Truy vấn UserCreatedAlbum thay vì Album
                return UserCreatedAlbum.objects.get(album_id=album_id)
            except UserCreatedAlbum.DoesNotExist:
                return None
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
    
    def to_representation(self, instance): # build URL đầy đủ cho ảnh
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if instance.image and request:
            rep['image'] = request.build_absolute_uri(instance.image.url)
        return rep


class AddTracksToAlbumSerializer(serializers.Serializer):
    # Không cần truyền album_id trong serializer vì nó đã được lấy từ URL (kwargs['album_id']) trong view.
    track_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
        write_only=True,
        help_text="Danh sách ID của các track sẽ được thêm vào album."
    )
