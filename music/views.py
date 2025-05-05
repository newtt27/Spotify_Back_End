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
from music.serializers.albums_serializers import AlbumSerializer, AlbumDetailSerializer
from music.serializers.artist_serializers import ArtistSerializer, ArtistDetailSerializer
from music.serializers.genre_serializers import GenreSerializer

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

class GetSongByGerneName(APIView):
    def get(self, request, genre_name):
        genre = get_object_or_404(Genre, name__iexact=genre_name) #Nếu tìm thấy thì trả về object, k thì trả về 404
        
        artists_in_genre = ArtistGenre.objects.filter(genre=genre).values_list('artist', flat=True) #Truy vấn artist theo thể loại
        if not artists_in_genre:
            return Response({"message": "No artists found for this genre."}, status=status.HTTP_404_NOT_FOUND)
        
        tracks = Track.objects.filter(artist__in=artists_in_genre) #Truy vấn nhạc theo thể loại
        if not tracks:
                return Response({"message": "No songs found for this genre."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TrackSerializer(tracks, many=True, context={'request': request})

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
        
        serializer = TrackSerializer(tracks, many=True, context={'request': request})

        response_data = {
            "songsBySearch": {
                "tracks": serializer.data,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)

class GetArtistDetails(APIView):
    def get(self, request, artist_name):
        artist = get_object_or_404(Artist, name__iexact=artist_name)
        #name__iexact: artist_name) #Tìm kiếm artist theo tên chính xác k phân biệt chữ hoa chữ thường
        serializer = ArtistDetailSerializer(artist)
        respones_data = {
            "artistDetails": serializer.data
        }
        return Response(respones_data, status=status.HTTP_200_OK)

class GetSongDetailsById(APIView):
    def get(self, request, track_id):
        track = get_object_or_404(Track, id=track_id)
        serializer = TrackSerializer(track, context={'request': request})
        response_data = {
            "songDetails": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

class GetSongRelated(APIView):
    def get(self, request, track_id):
        #Tìm thông tin bài hát theo track_id 
        try:
            track = Track.objects.select_related('artist').get(id=track_id)
        except Track.DoesNotExist:
            return Response({"error": "Track not found."}, status=status.HTTP_404_NOT_FOUND)
        
        artist = track.artist
        #Tìm các bài hát khác của cùng một nghệ sĩ
        same_artist_tracks = Track.objects.filter(artist=artist).exclude(id=track_id)[:5]

        #Tìm thể loại của ca sĩ
        artist_genres = ArtistGenre.objects.filter(artist=artist).values_list('genre', flat=True)
        #artist_genres = [1, 2] #Pop, R&B

        #Tìm các nghệ sĩ cùng thể loại
        related_artists = ArtistGenre.objects.filter(genre__in=artist_genres).exclude(artist=artist).values_list('artist', flat=True)

        #Tìm các bài hát của các nghệ sĩ liên quan
        related_tracks_by_genre = Track.objects.filter(artist__in=related_artists).exclude(id=track_id)[:5]
        #Gộp lại
        related_tracks = same_artist_tracks.union(related_tracks_by_genre)

        serializers = TrackSerializer(related_tracks, many=True)
        response_data = {
            "songRelated": {
                "tracks": serializers.data,
            }
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

        