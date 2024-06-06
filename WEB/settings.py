"""
Django settings for WEB project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
import sys
from pathlib import Path
import certifi
import environ
import google.auth
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from decouple import config




LEPTON_API_TOKEN = config('LEPTON_API_TOKEN')



if os.environ.get('PORT'):
    runserver_default_port = os.environ.get('PORT', '8000')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


if os.environ.get('PORT'):
    runserver_default_port = os.environ.get('PORT', '8000')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uy+4)+m@8mh+qck@&v!yr)8%lls6n=#wi4+5(7)c87dsp02-j$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True




ALLOWED_HOSTS = ['calm-connections.azurewebsites.net', '127.0.0.1']



SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = ['https://calm-connections.azurewebsites.net']

# Application definition

INSTALLED_APPS = [
    'WEB',
    'django.contrib.admin',
    'django.contrib.auth',
    'django_extensions',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_cron',
    'notifications',
    'issues',
    'drf_yasg',
    'httpcat',
    'allauth',
    'chat',
    'allauth.account',
    'storages',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'feedback',
    'Forum',
    'Progress',
    'Challenge',

]

SITE_ID = 2
SOCIALACCOUNT_LOGIN_ON_GET = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'WEB.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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




WSGI_APPLICATION = 'WEB.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


load_dotenv()
db_password = os.getenv('DB_PASSWORD')

environ.Env.read_env()

environ.Env.DB_SCHEMES['mssql'] = 'mssql'
env = environ.Env(DEBUG=(bool, False))

DEFAULT_DATABASE_URL = f'mssql://lkjhg13:{db_password}@calm-connections.database.windows.net/calm-connections?driver=ODBC+Driver+18+for+SQL+Server'

DATABASE_URL = os.environ.get('DATABASE_URL', DEFAULT_DATABASE_URL)
os.environ['DJANGO_DATABASE_URL'] = DATABASE_URL.format(**os.environ)

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    DATABASES = {
        'default': env.db('DJANGO_DATABASE_URL', default=DEFAULT_DATABASE_URL)
    }



AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend'
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SOCIAL_AUTH_GOOGLE_OAUTH2_UID_FIELD = 'google_id'





SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = '/static/'

# Define the directory where collectstatic will gather static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Define the directory where your static files are located
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]



###configuration for media file storing and reriving media file from gcloud


# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
#     }
# }
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     os.path.join(BASE_DIR, 'keys/credential.json')
# )
# GS_BUCKET_NAME = 'calm3861'

DJANGO_CRON_CLASSES = [
    'WEB.cron.EventNotificationCronJob',
]




DEFAULT_FILE_STORAGE = 'WEB.gcloud.GoogleCloudMediaFileStorage'
GS_PROJECT_ID = 'swift-reef-420509'
GS_BUCKET_NAME = 'calm3861'
MEDIA_ROOT = "media/"
UPLOAD_ROOT = 'media/uploads/'
MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)

JSON_KEY_FILE = os.path.join(BASE_DIR, 'keys', '../keys/credential.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = JSON_KEY_FILE

credentials, project = google.auth.default()
if credentials and credentials.expired and credentials.refresh_token:
    credentials.refresh(Request())

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

os.environ['SSL_CERT_FILE'] = certifi.where()



email_password: str = os.getenv('EMAIL_HOST_PASSWORD')



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'dima.bilik2005@gmail.com'
EMAIL_HOST_PASSWORD = email_password