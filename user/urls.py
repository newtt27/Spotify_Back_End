from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'), 
    path('register/', views.RegisterView.as_view(), name='user-register'),
]
