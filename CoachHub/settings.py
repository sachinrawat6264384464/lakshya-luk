import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# Security
# =========================
# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in productio
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')
DEBUG = True
ALLOWED_HOSTS = ["lakshya-luk.onrender.com","127.0.0.1"]


CSRF_TRUSTED_ORIGINS = ["https://lakshya-luk.onrender.com"]

# =========================
# Installed apps
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'EduTrack',
]

# =========================
# Middleware
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# Database (Railway PostgreSQL)
# =========================



BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': dj_database_url.config(
          default=os.environ.get("DATABASE_URL")
       
    )
}
# =========================
# URLs & WSGI
# =========================
ROOT_URLCONF = 'CoachHub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CoachHub.wsgi.application'

# =========================
# Password validation
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================
# Internationalization
# =========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# =========================
# Static files (production ready)
# =========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']        # local static folder
STATIC_ROOT = BASE_DIR / 'staticfiles'         # collectstatic folder
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =========================
# Default primary key
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
