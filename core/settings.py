# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from core import get_env, get_env_bool


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_VERSION = '1.0.0'

APP_NAME = 'Awesome App'

APP_URL = get_env('APP_URL', 'http://localhost')

SECRET_KEY = get_env('APP_KEY', 'somerandomstring')

DEBUG = get_env_bool('APP_DEBUG', False)

AUTH_USER_MODEL = 'common.User'

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fullurl',

    'common.apps.CommonConfig',
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Project specific
                'core.context_processors.settings_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env('DB_NAME', 'app'),
        'USER': get_env('DB_USERNAME', 'root'),
        'PASSWORD': get_env('DB_PASSWORD', ''),
        'HOST': get_env('DB_HOST', '127.0.0.1'),
        'PORT': get_env('DB_PORT', '3306'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = get_env('STATIC_URL', '/static/')

MEDIA_URL = get_env('MEDIA_URL', '/media/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public/static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'public/dist')

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
