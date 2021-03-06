# from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
import django

# admin.autodiscover()

urlpatterns = [
    url(r'', include('service.frontend.urls')),
    # url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^ckeditor/', include('ckeditor.urls')),
#    url(r'^feedback/', include('feedback.urls')),
    # url(r'^admin/doc/', include(django.contrib.admindocs.urls)),
    url(r'^admin/', include(admin.site.urls)),


    # url(r'^media/(?P<path>.*)$', include('django.views.static.serve'), {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', include('django.views.static.serve'), {'document_root': settings.STATIC_ROOT}),


    # url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
