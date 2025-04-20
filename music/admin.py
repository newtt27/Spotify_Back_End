from django.contrib import admin
from music.models import Track, Album, Artist, ArtistGenre, Genre

# Register your models here.
admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(ArtistGenre)
admin.site.register(Genre)