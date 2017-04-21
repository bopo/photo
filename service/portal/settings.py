from django.conf import settings
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT', os.path.join(HERE, 'media'))
THUMB_ROOT = getattr(settings, 'THUMB_ROOT', os.path.join(HERE, 'media', 'thumb'))
MEDIA_URL  = getattr(settings, 'MEDIA_URL', '/media/')
