from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('register/', views.RegisterView.as_view(), name='user-register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('me/', views.MeView.as_view(), name='me'),
    path('update/', views.UserUpdateView.as_view(), name='user-update'),
    # Sắp xếp từ cụ thể -> chung
    path('<int:user_id>/favourites/list/', views.UserFavouritesView.as_view(), name='user-favourite-track-list'),
    path('<int:user_id>/favourites/<int:track_id>/', views.UserFavouriteTrackDeleteView.as_view(), name='user-favourite-track-delete'),
    path('<int:user_id>/favourites/', views.UserFavouriteTrackCreateView.as_view(), name='user-favourite-track-create'),
    # userCreatedAlbum
    path('<int:id>/albums/', views.UserAlbumListView.as_view(), name='user-created-albums'),
    path('<int:id>/albums/create/', views.UserAlbumCreateView.as_view(), name='user-album-create'),
    path('albums/<str:album_id>/edit/', views.UserAlbumEditView.as_view(), name='user-album-edit'),
    path('albums/<str:album_id>/delete/', views.UserAlbumDeleteView.as_view(), name='delete-user-album'),
    path('<int:id>/albums/<str:album_id>/add-tracks/', views.AddTracksToUserAlbumView.as_view(), name='add-tracks-to-user-album'),
    # JWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
