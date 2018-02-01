# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from service.frontend.models import Photo

class KaifaItem(DjangoItem):
    django_model = Photo
    
    image_urls = scrapy.Field()
    file_urls = scrapy.Field()
    item_cats = scrapy.Field()
    item_tags = scrapy.Field()
    url = scrapy.Field()
    iid = scrapy.Field()