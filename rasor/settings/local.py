from .settings import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR.parent / 'assets',
]
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.parent / 'media'
