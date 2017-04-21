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
        'LOCATION': os.path.join(BASE_DIR, 'runtime/_cache'),
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

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    # 'django.middleware.locale.LocaleMiddleware',
    # 'django.middleware.cache.CacheMiddleware',
    # 'django.middleware.doc.XViewMiddleware',
    # 'django.middleware.gzip.GZipMiddleware',

    # 'minidetector.Middleware',
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
    'suit',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'easy_thumbnails',
    'service.portal',
    'mptt',

    'imagekit',
    'reversion',
    'import_export',
    'django_extensions',
)

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'media')
THUMB_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'media', 'thumb')


# 333

# Additional locations of static files
# STATICFILES_DIRS = (
#     os.path.join(STATIC_ROOT),
#     os.path.join(STATIC_ROOT, 'js'),
#     os.path.join(STATIC_ROOT, 'css'),
# )


# 333
# from django.conf.settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )

SUIT_CONFIG = {'ADMIN_NAME': '图片网站信息管理'}

ADMIN_MEDIA_PREFIX = '/media/'

# 333

THUMBNAIL_ALIASES = {
    '': {
        'thumb': {'size': (208, 291), 'crop': True},
        'rep': {'size': (254, 255), 'crop': True},
        'rep2': {'size': (203, 125), 'crop': True},
    },
}

TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [],
        # 'APP_DIRS': True,
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go ROOT_DIR
            ],
        },
    },
]

ALLOWED_HOSTS = ['*']
SITE_ID = 1
