from django.contrib import admin
from user.models import User, UserFavouriteTrack, UserCreatedAlbum, UserCreatedAlbumTrack
# Register your models here.
admin.site.register(User)
admin.site.register(UserFavouriteTrack)
admin.site.register(UserCreatedAlbum)
admin.site.register(UserCreatedAlbumTrack)
