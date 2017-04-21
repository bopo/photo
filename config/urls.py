# from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import django

# admin.autodiscover()

urlpatterns = (
    url(r'', include('service.portal.urls')),
    # url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^ckeditor/', include('ckeditor.urls')),
#    url(r'^feedback/', include('feedback.urls')),
    # url(r'^admin/doc/', include(django.contrib.admindocs.urls)),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),    
)
