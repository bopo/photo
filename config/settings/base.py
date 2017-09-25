# -*- coding: utf-8 -*-
# Django settings for testproject project.
import os
import sys
import environ

ROOT_DIR = environ.Path(__file__) - 3
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()

SECRET_KEY = env('DJANGO_SECRET_KEY', default='s4lk7ni)@9n0+4a!2_$vss8hqks_0#f_ia%i8k!djc87y$@0x5')

ALLOWED_HOSTS = ('*')

DEBUG = True

ADMINS = ()
MANAGERS = ADMINS

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, '..','runtime','_cache'),
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'locmem:///',
        'TIMEOUT': 60,
    },
    'redis': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '<host>:<port>',
        'OPTIONS': {'DB': 1, 'PASSWORD': 'yadayada', },
    },
}

SITE_ID = 1


USE_ETAGS = True

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


DATETIME_FORMAT = 'Y-m-d H:i:s'
HEADER_DATE_FORMAT = 'Y-m-d H:i:s'

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
)

# TEMPLATE_DIRS = (
# Put strings ROOT_DIR, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
#    os.path.join(ROOT_DIR, 'templates_plus'),
#    os.path.join(ROOT_DIR, 'templates'),
#)

ROOT_URLCONF = 'config.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',    
)

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

                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

ALLOWED_HOSTS = ['*']
SITE_ID = 1

try:
    from .cons import *
    from .apps import *
    from .suit import *

    from .static import *

    # from .celery import *
    # from .cache import *
    from .thumb import *

except ImportError as e:
    raise e
