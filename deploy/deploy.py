#coding=utf-8
import os, sys, django.core.handlers.wsgi

HERE = os.path.dirname(__file__)

sys.path.append(HERE)
sys.path.append(os.path.join(HERE, 'thirdparty'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'apps.settings'
application = django.core.handlers.wsgi.WSGIHandler()