import os
import django
# Thiết lập Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify_back_end.settings')
django.setup()

from music.models import Track, Album, Artist, ArtistGenre, Genre
from user.models import User, UserFavouriteTrack, UserCreatedAlbum, UserCreatedAlbumTrack

# Xóa tất cả các đối tượng trong bảng trước khi thêm mới
# Genre.objects.all().delete()
# Track.objects.all().delete()
# User.objects.filter(is_superuser=False).delete()
# Album.objects.all().delete()
# UserCreatedAlbum.objects.all().delete()
# UserCreatedAlbumTrack.objects.all().delete()
# Artist.objects.all().delete()
# ArtistGenre.objects.all().delete()

#Tạo gerne
pop = Genre.objects.create(name='Pop')
rock = Genre.objects.create(name='Rock')
RnB = Genre.objects.create(name='R&B')
classical = Genre.objects.create(name='Classical')
jazz = Genre.objects.create(name='Jazz')
hiphop = Genre.objects.create(name='Hip-Hop')
country = Genre.objects.create(name='Country')


#Tạo artist
artist1 = Artist.objects.create(
    name = 'Joji',
    image_url = 'images/artists/joji.jpg',
    followers = 1000000
)
artist2 = Artist.objects.create(
    name = 'Luke Chiang',
    image_url = 'images/artists/luke-chiang.jpg',
    followers = 2000000
)

#Tạo ArtistGenre
artist1_genre1 = ArtistGenre.objects.create(
    artist = artist1,
    genre = pop
)
artist1_genre2 = ArtistGenre.objects.create(
    artist = artist1,
    genre = RnB
)
#Tạo albums
album1 = Album.objects.create(
    name = 'Nectar',
    artist = artist1,
    image_url = 'images/albums/SMITHEREENS.jpg'
)

#Tạo tracks
track1 = Track.objects.create(
    name = 'Glimpse of Us',
    artist = artist1,
    album = album1,
    duration_ms = 200000,
    video_url = 'videos/Joji -  Glimpse of Us.mp4',
    views = 10000
)
track2 = Track.objects.create(
    name = 'Die For You',
    artist = artist1,
    album = album1,
    image_url = 'images/tracks/joji-glimpse-of-us.jpg',
    duration_ms = 180000,
    video_url = 'videos/Joji -  Die For You.mp4',
    views = 20000
)
track3 = Track.objects.create(
    name = 'Shouldnt Be',
    artist = artist2,
    album = album1,
    duration_ms = 240000,
    video_url = 'videos/Shouldnt Be.mp4',
    views = 30000
)

#Tạo User
user1 = User.objects.create_user(
    username = 'user1',
    password = 'password123',
    name = 'User One',
    email = 'user1@Gmail.com'
)
user2 = User.objects.create_user(
    username = 'user2',
    password = 'password123',
    name = 'User Two',
    email = 'user2@Gmail.com'
)
user3 = User.objects.create_user(
    username = 'user3',
    password = 'password123',
    name = 'User Three',
    email = 'user3@gmail.com'
)
user4 = User.objects.create_user(
    username = 'user4',
    password = 'password123',
    name = 'User Four',
    email = 'user4@gmail.com'
)

#Tạo UserFavouriteTrack
user_fav_track1 = UserFavouriteTrack.objects.create(
    user = user1,
    track = track1
)
user_fav_track2 = UserFavouriteTrack.objects.create(
    user = user1,
    track = track2
)
user_fav_track3 = UserFavouriteTrack.objects.create(
    user = user2,
    track = track1
)

#Tạo UserCreatedAlbum
user_created_album1 = UserCreatedAlbum.objects.create(
    album_id = 'album1',
    name = 'My Favorite Tracks',
    user = user3
)
user_created_album2 = UserCreatedAlbum.objects.create(
    album_id = 'album2',
    name = 'Chill Vibes',
    user = user4
)

#Tạo UserCreatedAlbum-Track
user_created_album_track1 = UserCreatedAlbumTrack.objects.create(
    album = user_created_album1,
    track = track1
)
user_created_album_track2 = UserCreatedAlbumTrack.objects.create(
    album = user_created_album1,
    track = track2
)
user_created_album_track3 = UserCreatedAlbumTrack.objects.create(
    album = user_created_album2,
    track = track3
)