"""
To switch between development and production environments:
Set the DJANGO_SETTINGS_MODULE variable in both wsgi.py, asgi.py and manage.py
to point to the correct settings file, e.g. 'myproject.settings.production'

Example for production:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.production')

Example for development:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.development')
"""

from .config import *
from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


INTERNAL_IPS = [
    "127.0.0.1", "https://schnack.up.railway.app/",
]

CSRF_TRUSTED_ORIGINS = [
    'https://schnack.up.railway.app/',
]
