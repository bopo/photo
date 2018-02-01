from django.conf.urls import include, url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from .feeds import RSS
from .models import Photo
from .views import *

info_dict = {
    'queryset': Photo.objects.all(),
    'date_field': 'created',
}

urlpatterns = (
    url(r'^$', home, name='home'), 
    url(r'^category/(?P<slug>\w+)', category, name='category'),
    url(r'^detail/(?P<id>\d+)', detail, name='detail'),
    url(r'^detail/(?P<id>\d+\.html)', detail, name='detail'),
    url(r'^tags/(?P<name>[\w|\s]+)', tags, name='tags'),
    url(r'^slide/(?P<swith>\w+)/(?P<id>\d+)', slide, name='slide'),
    url(r'^waterfall/(?P<id>\d+)', waterfall, name='slide'),
    url(r'^search', search, name='search'),
    url(r'^new.html', new, name='new'),
    url(r'^rec.html', rec, name='rec'),
    url(r'^hot.html', hot, name='hot'),
    url(r'^feed/rss$', RSS()),
    url(r'^feed/rss\.xml$', RSS()),
    url(r'^sitemap\.xml$', sitemap, {
        'sitemaps': {
            'photos': GenericSitemap(info_dict, priority=0.6)
        }
    }, name='django.contrib.sitemaps.views.sitemap'),
)
