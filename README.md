# SpotifyClone-Backend 🎵

Backend của dự án Spotify Clone – xây dựng bằng Django và PostgreSQL.

# API Endpoints 📌

Endpoint | Method | Name | Description
/music/topcharts/ | GET | get_top_charts | Retrieves a list of songs in the top charts.
/music/tracks/genre/<str:genre_name>/ | GET | get_songs_by_genre | Retrieves a list of songs belonging to a specific genre (genre_name).
/music/tracks/search/?q= | GET | get_songs_by_search | Searches for songs based on a keyword passed as a query parameter q.
/music/tracks/artist/<str:artist_name>/ | GET | get_songs_by_artist | Retrieves details about an artist and their songs (artist_name).

# Setup and Installation ⚙️

## 1. Create a Virtual Environment

- Run the following command:

```bash
  python -m venv myvenv
```

- Allow Script Execution in PowerShell (Windows)

```bash
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

- Activate the Virtual Environment

```bash
    myvenv\Scripts\activate
```

## 2. Install Required Libraries

- Run:

```bash
  pip install -r requirements.txt
```

## 3. Configure the Database

- Update the database settings in the settings.py file inside the spotify_clone_backend directory
- The project uses PostgreSQL as the database

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

## 4. Run Migrations

- Generate Migration Files from Models:

```bash
    python manage.py makemigrations
```

- Apply Migrations to the Actual Database:

```bash
    python manage.py migrate
```

## 5. Create an Admin (Superuser) Account

- Run:

```bash
    python manage.py createsuperuser
```

## 6. Run Seed Local Data:

- Run the following script to populate test data:

```bash
  py seeddata.py
```

## 7. Run the Server:

- Run:

```bash
    python manage.py runserver
```

## Some Useful Django Commands:

- Create a Django Project:

```bash
django-admin startproject 'project-name' .
```

- Create a Django App:

```bash
python manage.py startapp 'app-name'
```

# 📄LICENSE

- This project is licensed under the MIT License. See the LICENSE file for details.
