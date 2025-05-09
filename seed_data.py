import os
import django
# Thiết lập Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify_back_end.settings')
django.setup()

from music.models import Track, Album, Artist, Genre
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
Pop = Genre.objects.create(name='Pop')
RnB = Genre.objects.create(name='R&B')
Indie_Pop = Genre.objects.create(name='Indie Pop')
Lofi = Genre.objects.create(name='Lo-fi')
# Indie_Rock = Genre.objects.create(name='Indie Rock')
# Bedroom_Pop = Genre.objects.create(name='Bedroom Pop')
Alternative_RnB = Genre.objects.create(name='Alternative R&B')
Soul = Genre.objects.create(name='Soul')
Indie = Genre.objects.create(name='Indie')
# Trap = Genre.objects.create(name='Trap')
Lofi_Electropop = Genre.objects.create(name='Lo-fi Electropop')
Gospel = Genre.objects.create(name='Gospel')

#Tạo artist
artist1 = Artist.objects.create(
    name = 'Joji',
    image_url = 'images/artists/joji.jpg',
    followers = 1000000
)
artist2 = Artist.objects.create(
    name = 'Luke Chiang',
    image_url = 'images/artists/luke-chiang_lSTnFhJ.jpg',
    followers = 2000000
)
artist3 = Artist.objects.create(
    name = 'D4vd',
    image_url = 'images/artists/d4vd.jpg',
    followers = 3000000
)
artist4 = Artist.objects.create(
    name = 'Fran Vasilic',
    image_url = 'images/artists/franvasilic.jpg',
    followers = 4000000
)
artist5 = Artist.objects.create(
    name = 'RealestK',
    image_url = 'images/artists/realestk.jpg',
    followers = 500000
)

#Tạo albums
album1 = Album.objects.create(
    name = 'Nectar',
    artist = artist1,
    image_url = 'images/albums/SMITHEREENS.jpg'
)
album2 = Album.objects.create(
    name = 'WITHERED',
    artist = artist3,
    image_url = 'images/albums/WITHERED.png'
)
album3 = Album.objects.create(
    name = 'Dreams 2 Reality',
    artist = artist5,
    image_url = 'images/albums/Dreams2Reality.jpg'
)
album4 = Album.objects.create(
    name = 'Retrovisor',
    artist = artist4,
    image_url = 'images/albums/Retrovisor.jpg'
)

#Tạo tracks
track1 = Track.objects.create(
    name = 'Glimpse of Us',
    artist = artist1,
    album = album1,
    image_url = 'images/tracks/glimpse-of-us.jpg',
    duration_ms = 233000,
    video_url = 'videos/Joji -  Glimpse of Us.mp4',
    views = 10000
)
track2 = Track.objects.create(
    name = 'Die For You',
    artist = artist1,
    album = album1,
    image_url = 'images/tracks/die-for-you.jpg',
    duration_ms = 212000,
    video_url = 'videos/Joji -  Die For You.mp4',
    views = 20000
)
track3 = Track.objects.create(
    name = 'Shouldnt Be',
    artist = artist2,
    album = album1,
    image_url = 'images/tracks/shouldnt-be.jpg',
    duration_ms = 178000,
    video_url = 'videos/Shouldnt Be.mp4',
    views = 30000
)
track4 = Track.objects.create(
    name = 'Here with Me',
    artist = artist3,
    album = album2,
    image_url = 'images/tracks/herewithme.jpg',
    duration_ms = 232000,
    video_url = 'videos/d4vd - HereWithMe_d4vd.mp4',
    views = 40000
)
track5 = Track.objects.create(
    name = 'Sanctuary',
    artist = artist1,
    album = album1,
    image_url = 'images/tracks/sanctuary.jpg',
    duration_ms = 180000,
    video_url = 'videos/Joji - Sanctuary.mp4',
    views = 50000
)
track6 = Track.objects.create(
    name = 'Gimme Love',
    album = album1,
    artist = artist1,
    image_url = 'images/tracks/gimmelove.jpg',
    duration_ms = 214000,
    video_url = 'videos/Joji - Gimme Love.mp4',
    views = 60000
)
track7 = Track.objects.create(
    name = 'SLOW DANCING IN THE DARK',
    artist = artist1,
    album = album1,
    image_url = 'images/tracks/slowdancinginthedark.jpg',
    duration_ms = 209000,
    video_url = 'videos/Joji - SLOW DANCING IN THE DARK.mp4',
    views = 70000
)
track8 = Track.objects.create(
    name = 'Love Me',
    artist = artist5,
    album = album3,
    image_url = 'images/tracks/loveme.jpg',
    duration_ms = 186000,
    video_url = 'videos/RealestK - Love Me.mp4',
    views = 80000
)
track9 = Track.objects.create(
    name = 'Deja Vu',
    artist = artist5,
    album = album3,
    image_url = 'images/tracks/dejavu.jpg',
    duration_ms = 221000,
    video_url = 'videos/RealestK - Deja Vu.mp4',
    views = 90000
)
track10 = Track.objects.create(
    name = 'Hypotheticals',
    artist = artist4,
    album = album4,
    image_url = 'images/tracks/Hypotheticals.jpg',
    duration_ms = 212000,
    video_url = 'videos/Fran Vasilić - Hypotheticals.mp4',
    views = 100000
)
track11 = Track.objects.create(
    name = 'Television-So Far So Good',
    artist = artist4,
    album = album4,
    image_url = 'images/tracks/television.jpg',
    duration_ms = 194000,
    video_url = 'videos/Television _ So Far So Good.mp4',
)

#Tạo Genre cho Track
track1.genres.add(Pop, Alternative_RnB, Indie_Pop, Soul)
track2.genres.add(Pop, Indie_Pop, Soul, Lofi)
track3.genres.add(RnB, Soul, Indie_Pop, Lofi)
track4.genres.add(Pop, RnB, Indie_Pop, Lofi)
track5.genres.add(Lofi_Electropop, RnB, Pop, Soul, Lofi)
track6.genres.add(Indie_Pop, Soul, Pop, Gospel)
track7.genres.add(Alternative_RnB, Soul, Pop, Lofi)
track8.genres.add(Indie_Pop, RnB, Lofi)
track9.genres.add(Indie_Pop, RnB, Lofi, Soul)
track10.genres.add(Indie_Pop, Alternative_RnB)
track11.genres.add(Indie_Pop, Lofi)

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
user5 = User.objects.create_user(
    username = 'moctan137',
    password = 'password123',
    name = 'Nghĩa Tân',
    email = 'moctan137@gmail.com'
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
moctan_fav_track1 = UserFavouriteTrack.objects.create(
    user = user5,
    track = track6
) 
moctan_fav_track2 = UserFavouriteTrack.objects.create(
    user = user5,
    track = track9
) 
moctan_fav_track3 = UserFavouriteTrack.objects.create(
    user = user5,
    track = track11
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
moctan_created_album1 = UserCreatedAlbum.objects.create(
    album_id = 'album3',
    name = "Chill Songs",
    user = user5
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
moctan_created_album3_track1 = UserCreatedAlbumTrack.objects.create(
    album = moctan_created_album1,
    track = track4
)
moctan_created_album1_track2 = UserCreatedAlbumTrack.objects.create(
    album = moctan_created_album1,
    track = track10
)
moctan_created_album1_track3 = UserCreatedAlbumTrack.objects.create(
    album = moctan_created_album1,
    track = track8
)