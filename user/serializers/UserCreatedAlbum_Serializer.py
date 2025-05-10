from rest_framework import serializers
from user.models import UserCreatedAlbum
from music.models import Album, Artist  # để truy vấn thông tin album gốc
from music.serializers.tracks_serializers import TrackSerializer
import re  # dùng để tách số từ chuỗi

class UserCreatedAlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    artist_id = serializers.IntegerField(write_only=True, required=False)
    # image = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False, allow_null=True) # cho phép người dùng upload ảnh local (qua multipart/form-data).
    tracks = serializers.SerializerMethodField()

    class Meta:
        model = UserCreatedAlbum
        fields = ['album_id', 'name', 'artist', 'artist_id', 'image', 'tracks']
        read_only_fields = ['album_id', 'artist']  # Đảm bảo rằng album_id, artist chỉ để hiển thị (không yêu cầu từ client)

    def create(self, validated_data):
        # Lấy artist_id từ validated_data
        artist_id = validated_data.pop('artist_id', None)
        if not artist_id:
            raise serializers.ValidationError({'artist_id': 'This field is required.'})

        # Tạo album_id nếu không có
        album_id = self.context['request'].data.get('album_id', None)
        if not album_id:
            album_id = self.generate_unique_album_id()
        validated_data['album_id'] = album_id
        validated_data['user'] = self.context['request'].user  # nếu cần, đảm bảo rằng bạn gán đúng người dùng

        # # Nếu album_instance tồn tại, gán artist_id vào
        # album_instance = self.get_album_instance(album_id)
        # if album_instance:
        #     album_instance.artist_id = artist_id  # Cập nhật artist vào album
        #     album_instance.save()
        # else:
        #     # Nếu không có album, bạn cần tạo album mới
        #     validated_data['artist_id'] = artist_id  # Gán artist_id vào validated_data
        # Gán artist_id vào validated_data
        validated_data['artist_id'] = artist_id

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
    
    # def get_album_instance(self, album_id):
    #     pk = self.extract_album_pk(album_id)
    #     if pk is not None:
    #         try:
    #             return Album.objects.get(pk=pk)
    #         except Album.DoesNotExist:
    #             return None
    #     return None
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

    def get_artist(self, obj):
        # Sử dụng album_id để lấy Album gốc nếu cần, hoặc cũng có thể trả về từ artist_id
        album = self.get_album_instance(obj.album_id)
        if album and album.artist:
            return {
                'id': album.artist.id,
                'name': album.artist.name
            }
        elif hasattr(self, '_artist_id'):
            try:
                from music.models import Artist
                artist = Artist.objects.get(pk=self._artist_id)
                return {'id': artist.id, 'name': artist.name}
            except Artist.DoesNotExist:
                return None
        return None

    # def get_image(self, obj):
    #     album = self.get_album_instance(obj.album_id)
    #     if album and album.image_url:
    #         return self.build_absolute_uri(album.image_url.url)
    #     return None

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
