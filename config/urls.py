# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
import django

urlpatterns = (
    url(r'^', include('service.frontend.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^simditor/', include('simditor.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEBUG:
    urlpatterns += (url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),)
    
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += (url(r'^__debug__/', include(debug_toolbar.urls)),)
