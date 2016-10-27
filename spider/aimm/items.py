# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Item, Field
from category.models import Category, Tag
from apps.models import Photo


class AimmItem(DjangoItem):
    django_model = Photo

#    title = Field()
#    like = Field()
#    cover = Field()
#    images = Field()
#    pub_date = Field()
#    category = Field()
#    tags = Field()
    file_urls = Field()
    item_cats = Field()
    item_tags = Field()