"""
Django settings for dishproject project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SK"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_results",
    "django_celery_beat",
    "debug_toolbar",
    "dishes.apps.DishesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# DEBUG-TOOL-BAR
INTERNAL_IPS = ["127.0.0.1"]

ROOT_URLCONF = "dishproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dishproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Kiev"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "timedrotatig": {
            "format": "timedrotatig:{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "rotating": {
            "format": "rotating:{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file_timedrotating": {
            "level": "WARNING",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": BASE_DIR / "log.log",
            "when": "D",
            "interval": 1,
            "formatter": "timedrotatig",
            "backupCount": 1,
        },
        "file_rotating": {
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "log.log",
            "maxBytes": 1024*1024*5,
            "formatter": "rotating",
            "backupCount": 1,
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "dishes": {
            "handlers": ["file_timedrotating", "file_rotating", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# CELERY
from celery.schedules import crontab

CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = "Europe/Kiev"
CELERY_BROKER_URL = "redis://localhost"
CELERY_RESULT_BACKEND = "django-db"
CELERY_BEAT_SCHEDULE = {
    "report_every_day_at_22pm": {
        "task": "dishes.tasks.report",
        "schedule": crontab(hour=22, minute=0),
    }
}

# CACHE
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    },
}

# LOCALIZATION
LANGUAGES = [("en", "English"), ("ru", "Russian")]
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]


try:
    from .settings_local import *
except ImportError as e:
    print(e)


# FOR DEPLOYING ON HEROKU
###############################################################################
# import psycopg2
# import dj_database_url
#
# DEBUG = False
# ALLOWED_HOSTS = ["dishp.herokuapp.com"]
# MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# DATABASE_URL = os.environ["DATABASE_URL"]
# conn = psycopg2.connect(DATABASE_URL, sslmode="require")
# DATABASES = {
#     "default": dj_database_url.config(conn_max_age=600, ssl_require=True),
# }
