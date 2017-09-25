from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from .models import Photo


class PhotoViewSitemap(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Photo.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
