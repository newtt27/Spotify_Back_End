from django.urls import path
from music.views import GetTrackList

urlpatterns = [
    path('tracks/', GetTrackList.as_view(), name='get_track_list'),
]