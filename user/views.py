from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from user.models import User
from .models import UserFavouriteTrack
from .serializers.User_Serializer import UserSerializer
from .serializers.User_Register import UserRegisterSerializer
from .serializers.User_FavouriteTracks import UserFavouriteTrackSerializer

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

# POST
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Gắn session vào user
            return Response({"message": "Đăng nhập thành công"}, status=status.HTTP_200_OK)
        return Response({"error": "Sai tài khoản hoặc mật khẩu"}, status=status.HTTP_400_BAD_REQUEST)

# GET   
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"user": request.user.username})

# POST    
class LogoutView(APIView):
    def post(self, request):
        logout(request)  # Hủy session
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
        return Response(user_info, status=status.HTTP_200_OK)
    

# GET user favourites
class UserFavouritesView(APIView):
    def get(self, request, user_id):
        favourites = UserFavouriteTrack.objects.filter(user__id=user_id).select_related('track__artist', 'track__album')
        serializer = UserFavouriteTrackSerializer(favourites, many=True, context={'request': request})
        return Response(serializer.data)

# POST add to user favourites
class UserFavouriteTrackCreateView(APIView):
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
    def delete(self, request, user_id, track_id):
        try:
            fav = UserFavouriteTrack.objects.get(user__id=user_id, track_id=track_id)
            fav.delete()
            return Response({"detail": "Removed from favourites."}, status=status.HTTP_204_NO_CONTENT)
        except UserFavouriteTrack.DoesNotExist:
            return Response({"detail": "Track not found in favourites."}, status=status.HTTP_404_NOT_FOUND)