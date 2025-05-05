from .models import Track, Genre, Artist

def get_related_songs(track, limit=10):
    genres = Genre.objects.filter(artists__artist=track.artist).distinct()
    related_artists = Artist.objects.filter(genres__genre__in=genres).exclude(id=track.artist.id).distinct()
    related_tracks = Track.objects.filter(
        artist__in=related_artists
    ).exclude(id=track.id).distinct()[:limit]

    return related_tracks
