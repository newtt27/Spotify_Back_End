from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'), 
]
