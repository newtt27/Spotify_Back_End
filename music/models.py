from django.db import models

# Artist model
class Artist(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='images/artists/', blank=True, null=True)
    followers = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ['name']

    def __str__(self):
        return self.name


# Genre model
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ['name']

    def __str__(self):
        return self.name

# Album model
class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    image_url = models.ImageField(upload_to='images/albums/', blank=True, null=True)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} by {self.artist.name}"


# Track model
class Track(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tracks')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    duration_ms = models.IntegerField()
    # preview_url = models.URLField(max_length=255, blank=True, null=True)
    image_url = models.ImageField(upload_to='images/tracks/', blank=True, null=True)
    video_url = models.FileField(upload_to='videos/', blank=True, null=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} by {self.artist.name}"

# Artist-Genre relationship (many-to-many)
class ArtistGenre(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='genres')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='artists')

    class Meta:
        verbose_name = "Artist-Genre"
        verbose_name_plural = "Artist-Genres"
        unique_together = ('artist', 'genre')

    def __str__(self):
        return f"{self.artist.name} - {self.genre.name}"