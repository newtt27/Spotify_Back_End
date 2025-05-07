#Import các thư viện cần thiết
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
#Import các model và serializer cần thiết
from music.models import Track, Genre, Album, Artist
from music.serializers.tracks_serializers import TrackSerializer
from music.serializers.albums_serializers import AlbumSerializer, AlbumDetailSerializer
from music.serializers.artist_serializers import ArtistSerializer, ArtistDetailSerializer
from music.serializers.genre_serializers import GenreSerializer
#Import các utils cần thiết
from music.utils import get_related_songs_by_genre

# Create your views here.
class UpdateTrackViews(APIView):
    def patch(self, request, track_id):
        track = get_object_or_404(Track, id=track_id)
        track.views += 1
        track.save()
        return Response({"detail": "Track view count updated."}, status=status.HTTP_200_OK)
    
class GetTopCharts(APIView):
    def get(self, request):

        #Truy vấn nhạc
        # Sắp xếp theo số lượt nghe giảm dần và lấy 10 bản nhạc đầu tiên
        tracks = Track.objects.all().order_by('-views')[:10] #Thêm dấu '-' trước views để sắp xếp theo thứ tự giảm dần
        serializer = TrackSerializer(tracks, many=True, context={'request': request})

        top_charts = {
            "tracks": {
                "items": serializer.data,

            }
        }
        
        response_data = {
            "topCharts": top_charts,
        }
        return Response(response_data, status=status.HTTP_200_OK)

class GetSongByGenreID(APIView):
    def get(self, request, genre_id):
        genres = get_object_or_404(Genre, id=genre_id) #Nếu tìm thấy thì trả về object, k thì trả về 404
        
        track = Track.objects.filter(genres=genres) #Truy vấn nhạc theo thể loại
        if not track.exists(): #Nếu không có bài nào thì trả về 404
            return Response({"message": "No songs found for this genre."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TrackSerializer(track, many=True, context={'request': request}) #Serializer bài hát theo thể loại

        response_data = {
            "songsByGenre": {
                "tracks": serializer.data, #Trả về danh sách bài hát theo thể loại
            },
        }
        return Response(response_data, status=status.HTTP_200_OK)

class GetSongBySearchName(APIView):
    def get(self, request):
        # Lấy tham số tìm kiếm từ query string
        search_name = request.query_params.get('search_name', None)
        
        if search_name:
            # Truy vấn nhạc theo tên
            tracks = Track.objects.filter(Q(name__icontains=search_name)) 
        else:
            tracks = Track.objects.all() #Nếu không có tham số tìm kiếm thì lấy tất cả bài hát
            
        if not tracks.exists():
            return Response({"message": "No songs found for this name."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TrackSerializer(tracks, many=True, context={'request': request})

        response_data = {
            "songsBySearch": {
                "tracks": serializer.data,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)

class GetArtistDetailsById(APIView):
    def get(self, request, artist_id):
        artist = get_object_or_404(Artist, id=artist_id)
        serializer = ArtistDetailSerializer(artist)
        respones_data = {
            "artistDetails": serializer.data
        }
        return Response(respones_data, status=status.HTTP_200_OK)

class GetSongDetailsById(APIView):
    def get(self, request, track_id):
        track = get_object_or_404(Track, id=track_id)
        serializer = TrackSerializer(track, context={'request': request})
        songs_data = serializer.data #Lấy dữ liệu bài hát hiện tại bỏ vào dictionary sonsgs_data

        #Tìm các bài hát cùng genre với artist của bài hát hiện tại
        related_tracks = get_related_songs_by_genre(track, limit=5) #Lấy 5 bài hát liên quan
        related_tracks_serializer = TrackSerializer(related_tracks, many=True, context={'request': request})
        songs_data['relatedSongs'] = related_tracks_serializer.data  #Thêm các bài hát liên quan vào dữ liệu bài hát hiện tại


        response_data = {
            "songDetails": songs_data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
class GetAlbumList(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializers = AlbumDetailSerializer(albums, many=True)
        respone_data = {
            "albums": serializers.data
        }
        return Response(respone_data, status=status.HTTP_200_OK)

class GetGenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializers = GenreSerializer(genres, many=True)
        respone_data = {
            "genres": serializers.data
        }
        return Response(respone_data, status=status.HTTP_200_OK)