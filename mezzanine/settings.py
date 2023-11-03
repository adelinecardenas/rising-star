"""
Django settings for mezzanine project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import dj_database_url

from pathlib import Path
import django_heroku
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APPEND_SLASH = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s85)mgqbzhu_0^jml%q*dkxpyp$4n)ptji3zw)o(ve@*9tm*eh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
LOGIN_REDIRECT_URL = '/dashboard/login/'
LOGIN_URL = '/dashboard/login/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'main',
    'dashboard',
    'users',
    'crispy_forms',
    'mathfilters',

]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mezzanine.urls'
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
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

WSGI_APPLICATION = 'mezzanine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/dashboard/login/'

AUTH_USER_MODEL = 'users.CustomUser'
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

MEDIA_URL = "/media/"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
django_heroku.settings(locals())

# LIVE KEYS
# STRIPE_SECRET_KEY="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"
# STRIPE_PUBLISHABLE_KEY= "pk_live_51JXU1sJtDhAmrBJDgImxOEb35OhxnTuYSASsfol7xaDFFm2MfgCZOpsICDTgY5le9AdtnJ8JIkugKcCGqtxFJydz00VPli5F8E"
# STRIPE_ENDPOINT_SECRET ="whsec_K1O4f3EStNqstMuh5v7dAQMXvm2nCibX"

# TEST KEYS
STRIPE_SECRET_KEY = "sk_test_51JXU1sJtDhAmrBJD6tcH7pqwEYaDn264D0ttkpLQHKUI7giEkM9B2Btlt8QfXEyQwShJhv971EAg4CArAYu6vTp100IUWZZCdH"
STRIPE_PUBLISHABLE_KEY = "pk_test_51JXU1sJtDhAmrBJDin3SlmgUXHJqXpzKHzNyyLR0cThQ5HScrLBIqvQOWjgp8cHvp4fgN234Voij9L8OuGYhlOR0002bZBFNC6"
STRIPE_ENDPOINT_SECRET = "whsec_foBLtvYVg6WPOP5J7ag8ogifNN01g6LZ"
# local environment
# STRIPE_ENDPOINT_SECRET = "whsec_V55Pasa3RbsKnKo2YHAY7LtuH7kqI9x3"
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)