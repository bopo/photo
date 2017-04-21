# -*- coding: utf-8 -*-
# Django settings for testproject project.
import os
import sys
HERE = os.path.dirname(__file__)
# ASSETS = os.path.join(HERE, 'assets')

ALLOWED_HOSTS = ('*')

DEBUG = True

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(HERE, 'sqlite3.db'),
        # 'NAME': 'django',
        # 'USER': 'root',
        # 'PASSWORD': '123',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        # 'DEFAULT_CHARSET': 'utf8',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(HERE, 'runtime/_cache'),
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
SECRET_KEY = 'vaO4Y<g#YRWG8;Md8noiLp>.w(w~q_b=|1`?9<x>0KxA%UB!63'

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
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
#    os.path.join(HERE, 'templates_plus'),
#    os.path.join(HERE, 'templates'),
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
    # 'service.category',
    'service.portal',
    'mptt',
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/'

STATIC_ROOT = os.path.join(HERE,  'assets', 'static')
THUMB_ROOT = os.path.join(HERE, 'assets', 'media', 'thumb')
MEDIA_ROOT = os.path.join(HERE, 'assets', 'media')
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
        # 'DIRS': [],
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
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

ALLOWED_HOSTS = ['*']
SITE_ID = 1
