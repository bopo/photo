# from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls import include, url
# from .sitemap import PhotoViewSitemap
from . import feeds
from . import views
from . import sitemap

# sitemaps = {'static': sitemap.Sitemap,}

urlpatterns = (
  url(r'^$', views.home, name='home'), 
  url(r'^category/(?P<slug>\w+)', views.category, name='category'),
  url(r'^detail/(?P<id>\d+)', views.detail, name='detail'),
  url(r'^detail/(?P<id>\d+\.html)', views.detail, name='detail'),
  url(r'^tags/(?P<name>[\w|\s]+)', views.tags, name='tags'),
  url(r'^slide/(?P<swith>\w+)/(?P<id>\d+)', views.slide, name='slide'),
  url(r'^waterfall/(?P<id>\d+)', views.waterfall, name='slide'),
  url(r'^search', views.search, name='search'),
  url(r'^new.html', views.new, name='new'),
  url(r'^rec.html', views.rec, name='rec'),
  url(r'^hot.html', views.hot, name='hot'),
  url(r'^feed/rss\.xml$', feeds.RSS(), name='feed_rss_xml'),
  # url(r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap',
     # {'sitemaps': sitemaps}),
)
