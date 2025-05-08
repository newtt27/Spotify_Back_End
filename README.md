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

# Table of Contents - TOC

- [📌 API Endpoints](#api-endpoints-)
- [⚙️ Setup and Installation](#setup-and-installation-)
- [📄 License](#license-)

# API Endpoints 📌

**Base URL (local)**: `http://127.0.0.1:8000/api/`

| Endpoint                                         | Method | Params                                                     | Description                                                                                                                  |
| ------------------------------------------------ | ------ | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `/music/topcharts/`                              | GET    | –                                                          | Get top chart songs. Returns a list of tracks in the top charts.                                                             |
| `/music/tracks/<int:track_id>/play/`             | PATCH  | `track_id` in URL path                                     | Update track views. Increment the view count of a track by ID. Example: `/tracks/9/play`.                                    |
| `/music/genre/`                                  | GET    | –                                                          | Return a list of available music genres.                                                                                     |
| `/music/tracks/genre/<int:genre_id>/`            | GET    | `genre_id` in URL path                                     | Get songs by genre. Example: `/genre/10/`. Returns songs of the specified genre.                                             |
| `/music/tracks/search/`                          | GET    | `search_name` in query string                              | Search songs by name. Example: `?search_name=love`. Returns matching tracks.                                                 |
| `/music/artist/details/<int:artist_id>/`         | GET    | `artist_id` in URL path                                    | Get artist details and their top tracks and albums. Example: `/artist/1/`.                                                   |
| `/music/tracks/tracksdetail/<int:track_id>/`     | GET    | `track_id` in URL path                                     | Get full details of a specific song by ID and related songs (by genre). Example: `/tracksdetail/8/`.                         |
| `/music/tracks/albums/`                          | GET    | –                                                          | Get a list of all albums including artist info, image, and tracks.                                                           |
| `/user/`                                         | GET    | –                                                          | Get the list of users with detailed information. Returns a list of users.                                                    |
| `/user/register`                                 | POST   | JSON: `username`, `email`, `name`, `password`, `password2` | Register a new user after validating the provided information.                                                               |
| `/user/login`                                    | POST   | JSON: `username`, `password`                               | Login and create a session after validating the provided information.                                                        |
| `/user/logout`                                   | POST   | –                                                          | Logout and delete the current session.                                                                                       |
| `/user/me`                                       | GET    | –                                                          | Get personal information of the logged-in user. Returns the user’s information.                                              |
| `/user/<int:user_id>/favourites/`                | POST   | Path params: `user_id`, JSON: `track_id`                   | Add a track to the user's favourites list. Example: `/user/3/favourites/`.                                                   |
| `/user/<int:user_id>/favourites/<int:track_id>/` | DELETE | Path params: `user_id`, `track_id`                         | Remove a track from the user's favourites list. Example: `/user/3/favourites/1/`.                                            |
| `/user/<int:user_id>/favourites/list/`           | GET    | Path params: `user_id`                                     | Get all favourite tracks of a user. Returns full track info including artist and album. Example: `/user/3/favourites/list/`. |
| `/user/<int:id>/albums/`                         | GET    | Path params: `user_id`                                     | Get all custom albums created by the user. Returns album name, ID, artist, image, and tracks. Example: `/user/3/albums/`.    |
| `/user/<int:id>/albums/create/`                  | POST   | Path params: `user_id`, JSON: `name`                       | Create a new custom album. The album_id is auto-generated. Example: `/user/3/albums/create/`.                                |
| `/user/albums/<str:album_id>/rename/`            | PUT    | Path params: `album_id`, JSON: `name`                      | Rename a custom album. Example: `/user/albums/album2/rename/`.                                                               |
| `/user/albums/<str:album_id>/delete/`            | DELETE | Path params: `album_id`                                    | Delete a custom album created by the user. Example: `/user/albums/album2/delete/`.                                           |
| `/user/{user_id}/albums/{album_id}/add-tracks/`  | POST   | Path params: `user_id`, `album_id`, JSON: `track_ids`      | Add tracks to a custom album. Example: `/user/3/albums/album1/add-tracks/`, `{"track_ids": [1, 2, 3]}`.                      |
| `/user/token/refresh/`                           | POST   | JSON: `"refresh": "your_refresh_token_here"`               | Refresh the token for authentication.                                                                                        |

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
  py seed_data.py
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
