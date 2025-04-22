from django.urls import path
from music.views import GetTopCharts

urlpatterns = [
    path('topcharts/', GetTopCharts.as_view(), name='get_top_charts'),
]