"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url  # Make sure this is imported

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@%8+vzevbc+=iahavn#4ywwnj-gzj8g=41rh-r&&46l*ku=zfr'

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'pacific-brushlands-32121.herokuapp.com',
    'localhost',
    '127.0.0.1',
]

# ... your middleware and other settings ...

# Database - should be around line 75
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# If you have a static folder in your project
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Whitenoise for serving static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]