# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from .base import *
except ImportError as e:
    raise e

INSTALLED_APPS += (
    'service.frontend',
    'django_extensions',    

    'reversion',
    'imagekit',
)
