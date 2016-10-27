# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy import log

from aimm.items import AimmItem
from pprint import pprint
from os import path
import json, urllib

class MmSpider(BaseSpider):
    name = 'mm'
    allowed_domains = ['95mm.com']
    start_urls = [
        'http://www.95mm.com/category/qingchun/',
        'http://www.95mm.com/category/mingxing/',
        'http://www.95mm.com/category/wangluo/',
        'http://www.95mm.com/category/xinggan/',
        'http://www.95mm.com/category/mote/',
        'http://www.95mm.com/category/siwa/',
    ]

    def parse(self, response):
        hxs  = HtmlXPathSelector(response)
        base = path.dirname(response.url) + '/'
        urls = hxs.select('//div[@class="list-box"]/div[@class="preview"]/a')
        next = hxs.select('//div[@class="pages"]//li[@class="next"]/a')

        for url in urls:
            yield Request(url.select('@href').extract()[0].strip(), callback=lambda response, cover = url.select('img/@data-original').extract()[0].strip(): self.parseItem(response, cover))

        for link in next:
            if link.select('@href').extract()[0] != r'#':
                yield Request(base + link.select('@href').extract()[0].strip(), callback = self.parse)


    def parseItem(self, response, cover):
        item = AimmItem()
        sel = HtmlXPathSelector(response)
        pid = sel.select('//script').re(r'var pid="(\d+)";')

        item['title'] = sel.select('//span[@id="d_picTit"]/text()').extract()[0]
        item['cover'] = cover

        item['file_urls'] = 'http://www.95mm.com/slide-data/data/%s' % pid[0]
        item['item_cats'] = sel.select('//div[@class="post-header"]/div[@class="post-info clearfix"]/span/a/text()').extract()[0].strip()
        item['item_tags'] = sel.select('//span[@class="mod-tags"]/dl/dd/a/text()').extract()

        return item