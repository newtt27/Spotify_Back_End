# SpotifyClone-Backend 🎵

Phần backend của dự án **Spotify Clone**, được xây dựng bằng **Django** và **PostgreSQL**, hỗ trợ REST API, JWT, và cơ sở dữ liệu quan hệ.

Dự án này cung cấp các API để phát nhạc trực tuyến, bao gồm các tính năng như tìm kiếm bài hát, lấy bảng xếp hạng, lọc theo thể loại và truy xuất bài hát theo nghệ sĩ. Backend được thiết kế để xử lý các yêu cầu của người dùng và cung cấp dữ liệu âm nhạc phù hợp cho giao diện frontend.

# Mục lục - TOC
- [Tính Năng](#tính-năng)
- [Công nghệ](#công-nghệ)
- [Kiến trúc hệ thống](#Kiến-trúc-hệ-thống)
- [Cấu Trúc Dự Án](#cấu-trúc-dự-án)
- [Hướng Dẫn Sử Dụng](#hướng-dẫn-sử-dụng)
- [Các Endpoint API](#các-endpoint-api)
- [Bảo mật](#bảo-mật)
- [Thiết lập và Cài đặt](#thiết-lập-và-cài-đặt)
- [Giấy phép](#giấy-phép)
- [Đóng góp](#đóng-góp)

## Tính năng:

- ✅ Xác thực và quản lý người dùng bằng JWT
- 🔎 Tìm kiếm bài hát theo tên, thể loại hoặc nghệ sĩ
- 📊 Lấy bảng xếp hạng, danh sách album, chi tiết nghệ sĩ
- 🧩 Thiết kế RESTful, dễ tích hợp frontend
- ❤️ Quản lý bài hát yêu thích và album người dùng tạo

Backend tuân theo nguyên tắc RESTful API và được xây dựng dựa trên các tính năng mạnh mẽ của Django, đảm bảo khả năng mở rộng và linh hoạt.

## Công nghệ:

| Thành phần        | Công nghệ     |
|------------------|---------------|
| Backend          | Django 4.x    |
| API              | Django REST Framework |
| DB               | PostgreSQL    |
| Xác thực         | JWT (Simple JWT) |
| Test             | Postman |
| Ảnh/Media Upload | Pillow        |

## Kiến trúc hệ thống

Client (React, Mobile, v.v.)
    ↓
[REST API]
    ↓
Django + Django REST Framework
    ↓
PostgreSQL (Lưu trữ bài hát, user, album,...)


## Cấu Trúc Dự Án
```
spotify_backend/
├── spotify_back_end/                                     # Cấu hình toàn cục của Django project
│   ├── __init__.py                                       # Biến thư mục thành package Python
│   ├── asgi.py                                           # Cấu hình cho ASGI server
│   ├── settings.py                                       # Cấu hình chính (DB, apps, middleware...)
│   ├── urls.py                                           # Định tuyến chính toàn hệ thống
│   └── wsgi.py                                           # Cấu hình cho WSGI server
│
├── api/                                                  # App tổng hợp logic chung hoặc API gateway
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                                         # Model dùng chung nếu có
│   ├── tests.py
│   ├── urls.py                                           # Định tuyến cho các API trong app này
│   ├── views.py                                          # Xử lý các request/response API
│   └── migrations/                                       # Theo dõi thay đổi của model
│
├── music/                                                # Xử lý dữ liệu âm nhạc
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                                         # Model: Artist, Album, Track, Genre,...
│   ├── tests.py
│   ├── urls.py                                           # Định tuyến các API âm nhạc
│   ├── utils.py                                          # Hàm tiện ích xử lý dữ liệu nhạc
│   ├── views.py                                          # API trả danh sách bài hát, album, v.v.
│   ├── migrations/
│   └── serializers/                                      # Chuyển model -> JSON
│       ├── __init__.py
│       ├── albums_serializers.py                         # Serialize cho Album
│       ├── artist_serializers.py                         # Serialize cho Artist
│       ├── genre_serializers.py                          # Serialize cho thể loại nhạc
│       └── tracks_serializers.py                         # Serialize cho bài hát
│
├── user/                                                 # Quản lý người dùng và tương tác cá nhân
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                                         # User, FavouriteTrack, CreatedAlbum,...
│   ├── tests.py
│   ├── urls.py                                           # API đăng ký, đăng nhập, yêu thích...
│   ├── views.py
│   ├── migrations/
│   └── serializers/
│       ├── __init__.py
│       ├── User_FavouriteTracks.py                       # Serialize bài hát yêu thích
│       ├── User_Register.py                              # Xử lý đăng ký người dùng
│       ├── User_Serializer.py                            # Serialize profile người dùng
│       └── UserCreatedAlbum_Serializer.py                # Serialize album do người dùng tạo
│
├── media/                                                # Lưu file media được upload
│   ├── images/                                           # Ảnh (album, artist, avatar)
│   └── videos/                                           # Video âm nhạc (nếu có)
│
├── seed_data.py                                          # Script sinh dữ liệu mẫu
├── manage.py                                             # CLI Django: migrate, runserver, etc.
├── requirements.txt                                      # Thư viện cần cài (DRF, Pillow,...)
├── README.md                                             # Ghi chú hướng dẫn dự án
└── .gitignore                                            # Các file/thư mục không commit vào git
```

## Hướng Dẫn Sử Dụng
- **Phần mềm có thể sử dụng để test**: Postman 
- **Đăng Ký/Đăng Nhập**: Truy cập `/api/user/register/` để tạo tài khoản hoặc `/api/user/login/` để đăng nhập (ví dụ: `http://127.0.0.1:8000/api/user/login`). Sau đó, sử dụng JWT token được cấp để truy cập các chức năng cần permission.
- **Sử dụng các Endpoint API được liệt kê ở mục kế tiếp tùy theo mục đích**

## Các Endpoint API

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
| `/user/login/`                                   | POST   | JSON: `username`, `password`                                     | Đăng nhập và tạo phiên làm việc sau khi xác thực thông tin. Cung cấp access và refresh token (SimpleJWT), cấp quyền sử dụng các api liên quan.     |
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

## Bảo mật
- ✅ JWT Token + Refresh
- ✅ CSRF disabled for API-only
- ✅ CORS allowed origins qua cấu hình
- ✅ Image upload được giới hạn MIME
- 🔒 Không public endpoint nhạy cảm

## Thiết lập và Cài đặt

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
| Package                          | Mục đích chính                                                        |
| -------------------------------- | --------------------------------------------------------------------- |
| `Django==4.2.20`                 | Web framework chính                                                   |
| `djangorestframework==3.16.0`    | Xây dựng RESTful API                                                  |
| `djangorestframework_simplejwt`  | Xác thực người dùng bằng JWT (access/refresh token)                   |
| `drf-yasg==1.21.10`              | Tự động sinh tài liệu Swagger/OpenAPI cho API                         |
| `django-cors-headers==4.7.0`     | Hỗ trợ CORS cho phép gọi API từ frontend khác origin                  |
| `django-environ==0.12.0`         | Quản lý biến môi trường `.env` trong Django                           |
| `django-filter==25.1`            | Hỗ trợ lọc dữ liệu trong API (ví dụ: filter theo genre, artist, v.v.) |
| `django-allauth==65.7.0`         | Quản lý xác thực nâng cao (đăng nhập mạng xã hội, xác minh email,...) |
| `pillow==11.2.1`                 | Xử lý ảnh cho upload avatar, album cover, v.v.                        |
| `psycopg2==2.9.10`               | Trình kết nối PostgreSQL với Django                                   |
| `asgiref==3.8.1`                 | Hỗ trợ giao tiếp ASGI (cho ASGI server như Daphne, Channels nếu dùng) |
| `PyJWT==2.9.0`                   | Tạo và xác thực token JWT                                             |
| `inflection==0.5.1`              | Hỗ trợ chuyển đổi tên biến (ví dụ: camelCase ↔ snake\_case)           |
| `packaging==25.0`                | Định dạng & so sánh version, sử dụng nội bộ bởi các thư viện khác     |
| `pytz==2025.2`, `tzdata==2025.2` | Hỗ trợ timezone trong Python/Django                                   |
| `PyYAML==6.0.2`                  | Đọc và ghi file YAML, hỗ trợ cho Swagger hoặc config ngoài nếu có     |
| `sqlparse==0.5.3`                | Phân tích SQL, dùng trong Django admin hoặc migrations                |
| `typing_extensions==4.13.2`      | Cung cấp tính năng typing bổ sung cho Python < 3.10                   |
| `uritemplate==4.1.1`             | Phục vụ sinh route URL động trong tài liệu OpenAPI                    |

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

## LICENSE

- Dự án này được cấp phép theo giấy phép MIT. Xem file LICENSE để biết chi tiết.

## Đóng góp
Chúng tôi hoan nghênh mọi đóng góp! Để tham gia:
1. Fork kho lưu trữ.
2. Tạo nhánh tính năng (`git checkout -b feature/tinh-nang-moi`).
3. Commit thay đổi (`git commit -m 'Thêm tính năng mới'`).
4. Push lên nhánh (`git push origin feature/tinh-nang-moi`).
5. Mở Pull Request.