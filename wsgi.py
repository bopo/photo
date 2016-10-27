"""
WSGI config for pp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

HERE = os.path.dirname(__file__)

sys.path.append(HERE)
sys.path.append(os.path.join(HERE, 'thirdparty'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
# from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
# application = Sentry(application)

