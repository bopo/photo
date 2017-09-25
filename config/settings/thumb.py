# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from .base import *
except ImportError as e:
    raise e

INSTALLED_APPS += ('easy_thumbnails',)

THUMB_LIST = '500x500'
THUMB_DETAIL = '800x800'

THUMBNAIL_ALIASES = {
    '': {
        'thumb': {'size': (208, 291), 'crop': True},
        'rep': {'size': (254, 255), 'crop': True},
        'rep2': {'size': (203, 125), 'crop': True},
        'cov': {'size': (208, 291), 'crop': True},
    },
}