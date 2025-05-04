from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
import re

from music.models import Track
from user.models import User
from .models import UserFavouriteTrack, UserCreatedAlbum, UserCreatedAlbumTrack  
from .serializers.User_Serializer import UserSerializer
from .serializers.User_Register import UserRegisterSerializer
from .serializers.User_FavouriteTracks import UserFavouriteTrackSerializer
from .serializers.UserCreatedAlbum_Serializer import UserCreatedAlbumSerializer, AddTracksToAlbumSerializer

# API login + cấp token trong một bước duy nhất
from rest_framework_simplejwt.tokens import RefreshToken
    
# GET
class UserListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response({'users': serializer.data})

# POST
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST Login với JWT
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Xác thực người dùng
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Tạo refresh token và access token
            refresh = RefreshToken.for_user(user)
            
            # Lưu access_token vào session
            request.session['access_token'] = str(refresh.access_token)

            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'message': 'Đăng nhập thành công'
            }, status=status.HTTP_200_OK)

        return Response({"error": "Sai tài khoản hoặc mật khẩu"}, status=status.HTTP_400_BAD_REQUEST)

# GET   
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Lúc này, JWT sẽ tự động kiểm tra

    def get(self, request):
        return Response({"user": request.user.username})

# POST Logout - chỉ cần gửi phản hồi mà không cần logout
class LogoutView(APIView):
    def post(self, request):
        return Response({"message": "Đăng xuất thành công"}, status=status.HTTP_200_OK)
    
# GET
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_info = {
            "username": user.username,
            "email": user.email,
            "name": user.name,
        }

        # Gọi trực tiếp hàm xử lý nếu muốn tái sử dụng logic, không dùng HTTP
        # user_info['additional_data'] = some_internal_function(user)

        return Response(user_info, status=status.HTTP_200_OK)
        
# GET user favourites
class UserFavouritesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        favourites = UserFavouriteTrack.objects.filter(user__id=user_id).select_related('track__artist', 'track__album')
        serializer = UserFavouriteTrackSerializer(favourites, many=True, context={'request': request})
        return Response(serializer.data)

# POST add to user favourites
class UserFavouriteTrackCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        track_id = request.data.get('track_id')
        if not track_id:
            return Response({"detail": "Missing 'track_id'."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if UserFavouriteTrack.objects.filter(user=user, track_id=track_id).exists():
            return Response({"detail": "Track already in favourites."}, status=status.HTTP_400_BAD_REQUEST)

        UserFavouriteTrack.objects.create(user=user, track_id=track_id)
        return Response({"detail": "Added to favourites."}, status=status.HTTP_201_CREATED)

# DELETE remove from user favourites
class UserFavouriteTrackDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id, track_id):
        try:
            fav = UserFavouriteTrack.objects.get(user__id=user_id, track_id=track_id)
            fav.delete()
            return Response({"detail": "Removed from favourites."}, status=status.HTTP_204_NO_CONTENT)
        except UserFavouriteTrack.DoesNotExist:
            return Response({"detail": "Track not found in favourites."}, status=status.HTTP_404_NOT_FOUND)
        
#       user_created_album_views
# GET /user/{id}/albums/
class UserAlbumListView(generics.ListAPIView):
    serializer_class = UserCreatedAlbumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserCreatedAlbum.objects.filter(user__id=self.kwargs['id'])

# POST /user/{id}/albums/
class UserAlbumCreateView(generics.CreateAPIView):
    serializer_class = UserCreatedAlbumSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])
        data = request.data.copy()

        # Gọi serializer với data đã được cập nhật album_id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)  # Lưu user vào album

        return Response(serializer.data, status=status.HTTP_201_CREATED)



# PUT /albums/{album_id}/
class UserAlbumRenameView(generics.UpdateAPIView):
    queryset = UserCreatedAlbum.objects.all()
    serializer_class = UserCreatedAlbumSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'album_id'

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get('name', instance.name)
        instance.save()
        return Response(self.get_serializer(instance).data)

# DELETE /albums/{album_id}/
class UserAlbumDeleteView(generics.DestroyAPIView):
    queryset = UserCreatedAlbum.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'album_id'

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        if album.user != request.user:  # Kiểm tra quyền sở hữu
            return Response({"detail": "Bạn không có quyền xóa album này."}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

# POST /user/{id}/albums/{album_id}/add-tracks/
class AddTracksToUserAlbumView(generics.GenericAPIView):
    serializer_class = AddTracksToAlbumSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])
        album = get_object_or_404(UserCreatedAlbum, album_id=kwargs['album_id'], user=user) 

        # Kiểm tra quyền sở hữu
        if request.user != user:
            return Response(
                {"detail": "Bạn không có quyền thêm track vào album của người khác."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        track_ids = serializer.validated_data['track_ids']

        added_tracks = []
        existing_tracks = []
        invalid_tracks = []

        for track_id in track_ids:
            try:
                track = Track.objects.get(id=track_id)
                relation, created = UserCreatedAlbumTrack.objects.get_or_create(album=album, track=track)
                if created:
                    added_tracks.append(track_id)
                else:
                    existing_tracks.append(track_id)
            except Track.DoesNotExist:
                invalid_tracks.append(track_id)

        response_data = {
            "message": f"Đã thêm {len(added_tracks)} track vào album '{album.name}'.",
            "added_track_ids": added_tracks
        }

        if existing_tracks:
            response_data["existing_tracks"] = existing_tracks
        if invalid_tracks:
            response_data["invalid_tracks"] = invalid_tracks

        return Response(response_data, status=status.HTTP_200_OK)
