# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django

try:
    from .base import *
except ImportError as e:
    raise e

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    },
}

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        'drf_generators',
    )

    if django.VERSION > (1,10):
        MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    else:
        MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

    DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js'}
    DJANGO_SENTRY_DSN = env('DJANGO_SENTRY_DSN', default=None)

    if DJANGO_SENTRY_DSN:
        import raven
        INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
        RAVEN_CONFIG = {'dsn': DJANGO_SENTRY_DSN,}

