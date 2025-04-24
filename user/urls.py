from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'), 
    path('register/', views.RegisterView.as_view(), name='user-register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('me/', views.MeView.as_view(), name='me'),
]
