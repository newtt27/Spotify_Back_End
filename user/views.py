from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from .serializers.User_Serializer import UserSerializer

class UserListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response({'users': serializer.data})

