# SpotifyClone-Backend 🎵

The backend of the **Spotify Clone** project, built with **Django** and **PostgreSQL**.

This project provides APIs for music streaming, including features like searching songs, getting top charts, filtering by genre, and retrieving songs by artist. The backend is designed to handle user requests and deliver relevant music data to the frontend.

## Features:

- User authentication and management
- Music search by name, genre, or artist
- Top charts retrieval
- Integration with PostgreSQL database for efficient data storage

The backend follows RESTful API principles and is built with Django's robust features for scalability and flexibility.

**Technologies**:

- Backend Framework: Django
- Database: PostgreSQL
- API Protocol: REST

## API Endpoints 📌

**Base URL (local)**: `http://127.0.0.1:8000/api/`

| Endpoint                                  | Method | Params                        | Description                                                                  |
| ----------------------------------------- | ------ | ----------------------------- | ---------------------------------------------------------------------------- |
| `/music/topcharts/`                       | GET    | –                             | Get top chart songs. Returns a list of tracks in top charts.                 |
| `/music/tracks/genre/<str:genre_name>/`   | GET    | `genre_name` in URL path      | Get songs by genre. Example: `/genre/pop/`. Returns matching tracks.         |
| `/music/tracks/search/`                   | GET    | `search_name` in query string | Search songs by name. Example: `?search_name=love`. Returns matching tracks. |
| `/music/tracks/artist/<str:artist_name>/` | GET    | `artist_name` in URL path     | Get songs by artist. Example: `/artist/eminem/`. Returns artist & tracks.    |
| `/user/`                                  | GET    | -                             | Get the list of users with detailed information. Return the user list.       |
| `/user/register`                          | POST   | -                             | Validate information and create user.                                        |
| `/user/login`                             | POST   | -                             | Validate information and login. Create a session.                            |
| `/user/logout`                            | POST   | -                             | Validate information and logout. Delete current session.                     |
| `/user/me`                                | GET    | -                             | Personal information page. Return the user.                                  |
| `/user/<int:user_id>/favourites/`         | POST   | JSON with `track_id`          | Add a track to the user's favourites list. Example: `/user/3/favourites/`.                                  |
| `/user/<int:user_id>/favourites/<int:track_id>/`     | DELETE | –                             | Remove a track from the user's favourites list. Example: `/user/3/favourites/1/` .              |
| `/user/<int:user_id>/favourites/list/`    | GET    | –                             | Get all favourite tracks of a user. Returns full track info including artist album. Example: `/user/3/favourites/list/`.|
| `/users/<int:id>/albums/` | GET | – | Get all custom albums created by the user. Returns album name, ID, artist, image, and tracks. Example: `/users/3/albums/`.|
| `/users/<int:id>/albums/create/` | POST | JSON: name | Create a new custom album. The album_id is auto-generated (e.g., album5). Example: `/users/3/albums/create/`. |
| `/users/albums/<str:album_id>/rename/` | PUT | JSON: name | Rename a custom album. Example: `/users/albums/3/rename/`.  |
| `/users/albums/<str:album_id>/delete/` | DELETE | – | Delete a custom album created by the user. Example: `/users/albums/3/delete/`. |

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
