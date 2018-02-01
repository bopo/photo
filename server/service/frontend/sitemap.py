# sitemaps.py
from .models import Photo
from django.contrib.sitemaps import Sitemap

class PhotoSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Photo.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.created