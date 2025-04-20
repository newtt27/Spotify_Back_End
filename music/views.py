from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from music.models import Track
from music.serializers.tracks_serializers import TrackSerializer
# Create your views here.
class GetTrackList(APIView):
    def get(self, request):

        #Truy vấn nhạc
        tracks = Track.objects.all()
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