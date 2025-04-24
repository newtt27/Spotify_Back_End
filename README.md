# SpotifyClone-Backend 🎵

Backend của dự án Spotify Clone – xây dựng bằng Django và PostgreSQL.

## API Endpoints 📌

**Base URL (local)**: `http://127.0.0.1:8000/api/`

| Endpoint                                  | Method | Params                        | Description                                                                  |
| ----------------------------------------- | ------ | ----------------------------- | ---------------------------------------------------------------------------- |
| `/music/topcharts/`                       | GET    | –                             | Get top chart songs. Returns a list of tracks in top charts.                 |
| `/music/tracks/genre/<str:genre_name>/`   | GET    | `genre_name` in URL path      | Get songs by genre. Example: `/genre/pop/`. Returns matching tracks.         |
| `/music/tracks/search/`                   | GET    | `search_name` in query string | Search songs by name. Example: `?search_name=love`. Returns matching tracks. |
| `/music/tracks/artist/<str:artist_name>/` | GET    | `artist_name` in URL path     | Get songs by artist. Example: `/artist/eminem/`. Returns artist & tracks.    |

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
