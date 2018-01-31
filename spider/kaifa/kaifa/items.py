# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KaifaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    
    file_urls = scrapy.Field()
    item_cats = scrapy.Field()
    item_tags = scrapy.Field()