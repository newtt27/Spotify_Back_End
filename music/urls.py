from django.urls import path
from music.views import GetTopCharts, GetSongByGerneName, GetSongBySearchName, GetArtistDetails, GetSongDetails, GetSongRelated, GetAlbumList, UpdateTrackViews

urlpatterns = [
    path('tracks/<int:track_id>/play/', UpdateTrackViews.as_view(), name='update_track_views'),
    path('topcharts/', GetTopCharts.as_view(), name='get_top_charts'),
    path('tracks/genre/<str:genre_name>/', GetSongByGerneName.as_view(), name='get_songs_by_genre'),  
    path('tracks/search/', GetSongBySearchName.as_view(), name='get_songs_by_search'),
    path('tracks/artist/<str:artist_name>/', GetArtistDetails.as_view(), name='get_songs_by_artist'),
    path('tracks/tracksdetail/<int:track_id>/', GetSongDetails.as_view(), name='get_songs_by_track_id'),
    path('tracks/related-song/<int:track_id>/', GetSongRelated.as_view(), name='get_related_songs'),
    path('tracks/albums/', GetAlbumList.as_view(), name='get_album_list'),
]