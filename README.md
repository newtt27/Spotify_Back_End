# SpotifyClone-Backend 🎵

Backend của dự án Spotify Clone – xây dựng bằng Django và PostgreSQL.

# API Endpoints

# Setup and Installation

## 1. Create a Virtual Environment

```bash
python -m venv myvenv
```

### 1.1 Allow Script Execution in PowerShell (Windows)

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### 1.2 Activate the Virtual Environment

    myvenv\Scripts\activate

## 2. Install Required Libraries

    pip install -r requirements.txt

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

### 4.1 Generate Migration Files from Models:

    python manage.py makemigrations

### 4.2 Apply Migrations to the Actual Database:

    python manage.py migrate

## 5. Create an Admin (Superuser) Account

    python manage.py createsuperuser

## 6. Run Seed Local Data:

    py seeddata.py

## 7. Run the Server:

    python manage.py runserver

## Some Useful Django Commands:

- Create a Django Project:

```bash
django-admin startproject 'project-name' .
```

- Create a Django App:

```bash
python manage.py startapp 'app-name'
```

# LICENSE

- This project is licensed under the MIT License. See the LICENSE file for details.
