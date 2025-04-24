from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'), 
    path('register/', views.RegisterView.as_view(), name='user-register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('me/', views.MeView.as_view(), name='me'),
    # Sắp xếp từ cụ thể -> chung
    path('<int:user_id>/favourites/list/', views.UserFavouritesView.as_view(), name='user-favourite-track-list'),
    path('<int:user_id>/favourites/<int:track_id>/', views.UserFavouriteTrackDeleteView.as_view(), name='user-favourite-track-delete'),
    path('<int:user_id>/favourites/', views.UserFavouriteTrackCreateView.as_view(), name='user-favourite-track-create'),

]
