from .models import Track, Genre, Artist

def get_related_songs_by_genre(track, limit=5):
    track_genres =  Track.objects.filter(id=track.id).values_list('genres', flat=True) #Lấy tất cả các thể loại của bài hát hiện tại
    related_tracks = Track.objects.filter(genres__in=track_genres).exclude(id=track.id).distinct().order_by('?')[:limit] #Lấy ngẫu nhiên bài hát cùng thể loại với bài hát hiện tại
    return related_tracks


# Xây dựng URL tuyệt đối từ đường dẫn tương đối.
def convert_to_absolute_url(request, relative_path):
    if request is not None and relative_path:
        return request.convert_to_absolute_url(relative_path)
    return relative_path