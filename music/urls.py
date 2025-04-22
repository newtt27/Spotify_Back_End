from django.urls import path
from music.views import GetTopCharts, GetSongByGerneName, GetSongBySearchName, GetArtistDetails

urlpatterns = [
    path('topcharts/', GetTopCharts.as_view(), name='get_top_charts'),
    path('tracks/genre/<str:genre_name>/', GetSongByGerneName.as_view(), name='get_songs_by_genre'),  
    path('tracks/search/', GetSongBySearchName.as_view(), name='get_songs_by_search'),
    path('tracks/artist/<str:artist_name>/', GetArtistDetails.as_view(), name='get_songs_by_artist'),
]