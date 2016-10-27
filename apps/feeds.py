# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.core.cache import cache

from .models import Photo


class RSS(Feed):
    title = u"蜜糖剧集站"
    link = "http://www.mi-tang.com"
    description = u"蜜糖剧集站 百度影音 快播高清"

    def items(self):
        items = cache.get('items')

        if items == None:
            items = Photo.objects.order_by('-pub_date')[:20]
            cache.set('items', items, 30)

        return items

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.cover

    def item_link(self, item):
        return reverse('detail', args=[item.pk])
