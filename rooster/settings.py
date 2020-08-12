"""
Django settings for rooster project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
from decouple import config
import decouple

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v(5xdt)+ybk!2!-o=+#&@f$%mh98qu2hkhy!_6l36u&cyom!-)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms",
    'roost',
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

ROOT_URLCONF = 'rooster.urls'

AUTH_USER_MODEL = "roost.user"

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
            ],
        },
    },
]

WSGI_APPLICATION = 'rooster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media")
MEDIA_URL = "/media/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'jamescndubuisi@zohomail.com'
EMAIL_HOST_PASSWORD = 'fK3Nhh44RD59'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Educate <jamescndubuisi@zohomail.com>'
LOGIN_URL = 'log_in'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "log_in"
CRISPY_TEMPLATE_PACK = "bootstrap4"


# Test mode
PAYSTACK_PUBLIC_KEY = "pk_test_bcd5df0ff5d086e88c29302cce1b9742733c23d3"
PAYSTACK_SECRET_KEY = "sk_test_2332bf8719a9af3f8df1315c12b26e2822012cfc"
PAYSTACK_SUCCESS_URL = "/"
PAYSTACK_FAILED_URL = "/pay"
if not DEBUG:
    SECRET_KEY = config('SECRET_KEY')
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL'),
            conn_max_age=500
        )
    }