# SpotifyClone-Backend 🎵

Backend của dự án Spotify Clone – xây dựng bằng Django và PostgreSQL.

## ✅ 1. Tạo môi trường ảo

```bash
python -m venv myvenv
```

### 1.1 Mở quyền chạy Scripts trên PowerShell (Windows)

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### 1.2 Kích hoạt môi trường ảo

    myvenv\Scripts\activate

## ✅ 2.Cài đặt các thư viện cần thiết

    pip install -r requirements.txt

## ✅ 3.Cấu hình lại database:

- Cấu hình lại database trong file settings.py của spotify_clone_backend
- Database dùng PostgreSQL

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

## ✅ 4. Migrate

### 4.1 Tạo migrations từ các Model dưới dạngPythoncode:

    python manage.py makemigrations

### 4.2 Thực hiện các migration đó trên database thật:

    python manage.py migrate

## ✅ 5. Tạo tài khoản quản trị (superuser)

    python manage.py createsuperuser

## ✅ 6. Chạy server:

    python manage.py runserver

## Một số lệnh Django hữu ích:

- Tạo project Django:

```bash
django-admin startproject 'project-name' .
```

- Tạo một app:

```bash
python manage.py startapp 'app-name'
```