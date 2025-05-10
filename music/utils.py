from .models import Track, Genre, Artist
import random

def get_related_songs_by_genre(track, limit=5):
    track_genres = track.genres.values_list('id', flat=True)

    # Lấy danh sách ID bài hát không trùng
    related_track_ids = (
        Track.objects
        .filter(genres__in=track_genres)
        .exclude(id=track.id)
        .values_list('id', flat=True)
        .distinct()
    )

    selected_ids = random.sample(list(related_track_ids), min(limit, len(related_track_ids)))
    return Track.objects.filter(id__in=selected_ids)

