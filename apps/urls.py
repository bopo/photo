# from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls import include, url
# from .sitemap import PhotoViewSitemap
from .feeds import RSS
from .views import *

# sitemaps = {'static': PhotoViewSitemap, }

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
  # url(r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap',
     # {'sitemaps': sitemaps}),
)
