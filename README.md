# SpotifyClone-Backend 🎵

Phần backend của dự án **Spotify Clone**, được xây dựng bằng **Django** và **PostgreSQL**.

Dự án này cung cấp các API để phát nhạc trực tuyến, bao gồm các tính năng như tìm kiếm bài hát, lấy bảng xếp hạng, lọc theo thể loại và truy xuất bài hát theo nghệ sĩ. Backend được thiết kế để xử lý các yêu cầu của người dùng và cung cấp dữ liệu âm nhạc phù hợp cho giao diện frontend.

## Tính năng:

- Xác thực và quản lý người dùng
- Tìm kiếm bài hát theo tên, thể loại hoặc nghệ sĩ
- Lấy bảng xếp hạng các bài hát
- Tích hợp với cơ sở dữ liệu PostgreSQL để lưu trữ dữ liệu hiệu quả

Backend tuân theo nguyên tắc RESTful API và được xây dựng dựa trên các tính năng mạnh mẽ của Django, đảm bảo khả năng mở rộng và linh hoạt.

**Công nghệ**:

- Framework Backend: Django
- Cơ sở dữ liệu: PostgreSQL
- Giao thức API: REST

# Mục lục - TOC

- [📌 Các Endpoint API](#api-endpoints-)
- [⚙️ Thiết lập và Cài đặt](#setup-and-installation-️)
- [📄 Giấy phép](#license-)

# Các Endpoint API 📌

**Base URL (cục bộ)**: `http://127.0.0.1:8000/api/`

| Endpoint                                         | Method | Params                                                           | Description                                                                                                                  |
| ------------------------------------------------ | ------ | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `/music/topcharts/`                              | GET    | –                                                                | Lấy danh sách các bài hát nằm trong bảng xếp hạng.                                                             |
| `/music/tracks/<int:track_id>/play/`             | PATCH  | `track_id` in URL path                                           | Cập nhật số lượng view của một track. Tăng số lượt nghe của bài hát có ID tương ứng. Ví dụ: `/tracks/9/play`.                                    |
| `/music/genre/`                                  | GET    | –                                                                | Trả về danh sách các thể loại nhạc hiện có.                                                                                     |
| `/music/tracks/genre/<int:genre_id>/`            | GET    | `genre_id` in URL path                                           | Lấy danh sách bài hát theo thể loại. Ví dụ: `/genre/10/`.                                             |
| `/music/tracks/search/`                          | GET    | `search_name` in query string                                    | Tìm kiếm bài hát theo tên. Ví dụ: `?search_name=love`.                                                |
| `/music/artist/details/<int:artist_id>/`         | GET    | `artist_id` in URL path                                          | Trả về chi tiết nghệ sĩ và các bài hát, album nổi bật của họ. Ví dụ: `/artist/1/`.                                                   |
| `/music/tracks/tracksdetail/<int:track_id>/`     | GET    | `track_id` in URL path                                           | Trả về chi tiết bài hát và các bài hát liên quan (theo thể loại). Ví dụ: `/tracksdetail/8/`.                         |
| `/music/tracks/albums/`                          | GET    | –                                                                | Lấy danh sách tất cả các album bao gồm thông tin nghệ sĩ, hình ảnh và bài hát.                                                           |
| `/music/tracks/download/<int:track_id>`          | GET    | `track_id` in URL path                                           | Tải tệp phương tiện (mp4) của bài hát theo ID.                                                                 |
| `/user/`                                         | GET    | –                                                                | Lấy danh sách người dùng cùng thông tin chi tiết.                                                    |
| `/user/register/`                                | POST   | JSON: `username`, `email`, `name`, `password`, `password2`       | Đăng ký người dùng mới sau khi xác thực thông tin.                                                               |
| `/user/login/`                                   | POST   | JSON: `username`, `password`                                     | Đăng nhập và tạo phiên làm việc sau khi xác thực thông tin.                                                        |
| `/user/logout/`                                  | POST   | –                                                                | Đăng xuất và xóa phiên làm việc hiện tại.                                                                                       |
| `/user/me/`                                      | GET    | –                                                                | Lấy thông tin cá nhân của người dùng đã đăng nhập.                                              |
| `/user/update/`                                  | PATCH  | JSON: `name`         |                                           | Cập nhật tên người dùng. |
| `/user/<int:user_id>/favourites/`                | POST   | Path params: `user_id`, JSON: `track_id`                         | Thêm bài hát vào danh sách yêu thích của người dùng. Ví dụ: `/user/3/favourites/`.                                                   |
| `/user/<int:user_id>/favourites/<int:track_id>/` | DELETE | Path params: `user_id`, `track_id`                               | Xóa bài hát khỏi danh sách yêu thích. Ví dụ: `/user/3/favourites/1/`.                                            |
| `/user/<int:user_id>/favourites/list/`           | GET    | Path params: `user_id`                                           | Lấy tất cả bài hát yêu thích của người dùng (bao gồm thông tin artist và album). Ví dụ: `/user/3/favourites/list/`. |
| `/user/<int:id>/albums/`                         | GET    | Path params: `user_id`                                           |Lấy tất cả album tùy chỉnh mà người dùng đã tạo (album name, ID, artist, image, và tracks). Ví dụ: `/user/3/albums/`.    |
| `/user/<int:id>/albums/create/`                  | POST   | Path params: `user_id`, form-data: `name`, `artist_id`, `image (file upload)` | Tạo album tùy chỉnh mới. `album_id` sẽ được tạo tự động. Ví dụ: `/user/3/albums/create/`.                                |
| `/user/albums/<str:album_id>/edit/`              | PATCH    | Path params: `album_id`, form-data: `name`, `image (file upload)`  | Đổi tên album tùy chỉnh. Ví dụ: `/user/albums/album2/rename/`.                                                               |
| `/user/albums/<str:album_id>/delete/`            | DELETE | Path params: `album_id`                                          | Xóa album tùy chỉnh của người dùng. Ví dụ: `/user/albums/album2/delete/`.                                           |
| `/user/{user_id}/albums/{album_id}/add-tracks/`  | POST   | Path params: `user_id`, `album_id`, JSON: `track_ids`            | Thêm các bài hát vào album tùy chỉnh. Ví dụ: `/user/3/albums/album1/add-tracks/`, `{"track_ids": [1, 2, 3]}`.                      |
| `/user/token/refresh/`                           | POST   | JSON: `"refresh": "your_refresh_token_here"`                     | Làm mới token xác thực.                                                                                        |

# Thiết lập và Cài đặt ⚙️

## 1. Tạo Môi Trường Ảo (Virtual Environment)

- Chạy lệnh sau:

```bash
  python -m venv myvenv
```

- Cho phép thực thi script trong PowerShell (Windows):

```bash
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

- Kích hoạt môi trường ảo:

```bash
    myvenv\Scripts\activate
```

## 2. Cài đặt Thư viện Cần Thiết

- Chạy:

```bash
  pip install -r requirements.txt
```

## 3. Cấu Hình Cơ Sở Dữ Liệu

- Cập nhật cấu hình cơ sở dữ liệu trong file settings.py bên trong thư mục spotify_clone_backend.
- Dự án sử dụng PostgreSQL làm cơ sở dữ liệu:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spotify_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 4. Thực hiện Migrations

- Tạo file migration từ models::

```bash
    python manage.py makemigrations
```

- Áp dụng migrations vào cơ sở dữ liệu::

```bash
    python manage.py migrate
```

## 5. Tạo Tài Khoản Quản Trị (Superuser)

- Chạy:

```bash
    python manage.py createsuperuser
```

## 6. Tạo Dữ Liệu Mẫu Cục Bộ:

- Chạy script sau để tạo dữ liệu thử nghiệm:

```bash
  py seed_data.py
```

## 7. Chạy Server:

- Chạy:

```bash
    python manage.py runserver
```

## Một số lệnh Django hữu ích:

- Tạo một project Django:

```bash
django-admin startproject 'project-name' .
```

- Tạo một app Django:

```bash
python manage.py startapp 'app-name'
```

# LICENSE 📄

- Dự án này được cấp phép theo giấy phép MIT. Xem file LICENSE để biết chi tiết.
