#Import các thư viện cần thiết
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
#Import các model và serializer cần thiết
from music.models import Track, Genre, Album, Artist, ArtistGenre
from music.serializers.tracks_serializers import TrackSerializer
from music.serializers.albums_serializers import AlbumSerializer
from music.serializers.artist_serializers import ArtistSerializer, ArtistDetailSerializer
from music.serializers.genre_serializers import GenreSerializer

# Create your views here.
class GetTopCharts(APIView):
    def get(self, request):

        #Truy vấn nhạc
        # Sắp xếp theo số lượt nghe giảm dần và lấy 10 bản nhạc đầu tiên
        tracks = Track.objects.all().order_by('-views')[:10] #Thêm dấu '-' trước views để sắp xếp theo thứ tự giảm dần
        serializer = TrackSerializer(tracks, many=True)

        top_charts = {
            "tracks": {
                "items": serializer.data,

            }
        }
        
        response_data = {
            "topCharts": top_charts,
        }
        return Response(response_data, status=status.HTTP_200_OK)

class GetSongByGerneName(APIView):
    def get(self, request, genre_name):
        genre = get_object_or_404(Genre, name__iexact=genre_name) #Nếu tìm thấy thì trả về object, k thì trả về 404
        
        artists_in_genre = ArtistGenre.objects.filter(genre=genre).values_list('artist', flat=True) #Truy vấn artist theo thể loại
        if not artists_in_genre:
            return Response({"message": "No artists found for this genre."}, status=status.HTTP_404_NOT_FOUND)
        
        tracks = Track.objects.filter(artist__in=artists_in_genre) #Truy vấn nhạc theo thể loại
        if not tracks:
                return Response({"message": "No songs found for this genre."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TrackSerializer(tracks, many=True)

        response_data = {
            "songsByGenre": serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
class GetSongBySearchName(APIView):
    def get(self, request):
        # Lấy tham số tìm kiếm từ query string
        search_name = request.query_params.get('search_name', None)
        
        if not search_name:
            return Response({"detail": "No search name provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Truy vấn nhạc theo tên
        tracks = Track.objects.filter(Q(name__icontains=search_name))  # Truy vấn nhạc theo tên bài hát
        
        if not tracks.exists():
            return Response({"message": "No songs found for this name."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TrackSerializer(tracks, many=True)

        response_data = {
            "songsBySearch": {
                "tracks": serializer.data,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)

class GetArtistDetails(APIView):
    def get(self, request, artist_name):
        artist = get_object_or_404(Artist, name=artist_name)
        serializer = ArtistDetailSerializer(artist)
        respones_data = {
            "artistDetails": serializer.data
        }
        return Response(respones_data, status=status.HTTP_200_OK)
