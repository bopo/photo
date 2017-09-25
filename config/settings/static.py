# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from .base import *
except ImportError as e:
    raise e

MEDIA_URL = env('DJANGO_MEDIA_URL', default='/media/')
STATIC_URL = env('DJANGO_STATIC_URL', default='/static/')

STATIC_HOST = env('DJANGO_STATIC_HOST', default='')
STATIC_URL = STATIC_HOST + STATIC_URL
MEDIA_URL = STATIC_HOST + MEDIA_URL

ADMIN_MEDIA_PREFIX = '/media/'

# STATIC_HOST = 'http://static.moo.life' if not DEBUG else ''
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'static')

MEDIA_ROOT = str(ROOT_DIR('assets/media'))
THUMB_ROOT = str(ROOT_DIR('assets/media/thumb'))
THUMB_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'media','thumb')

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
