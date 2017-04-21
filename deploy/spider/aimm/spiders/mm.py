# -*- coding: utf-8 -*-
# from scrapy.selector import HtmlXPathSelector
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.spiders import Spider
# from scrapy.http import Request
# from scrapy import log
import scrapy
from aimm.items import AimmItem
# from pprint import pprint
# from os import path
# import json, urllib

class MmSpider(scrapy.Spider):
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
        # hxs  = HtmlXPathSelector(response)
        # base = path.dirname(response.url) + '/'
        urls = response.xpath('//div[@class="list-box"]/div[@class="preview"]/a')
        next = response.xpath('//div[@class="pages"]//li[@class="next"]/a')

        for url in urls:
            yield scrapy.Request(url.select('@href').extract()[0].strip(), callback=lambda response, cover = url.select('img/@data-original').extract()[0].strip(): self.parseItem(response, cover))

        for link in next:
            if link.select('@href').extract()[0] != r'#':
                yield scrapy.Request(response.urljoin(link.select('@href').extract()[0].strip()), callback = self.parse)


    def parseItem(self, response, cover):
        item = AimmItem()
        # sel = HtmlXPathSelector(response)
        pid = response.xpath('//script').re(r'var pid="(\d+)";')

        item['title'] = response.xpath('//span[@id="d_picTit"]/text()').extract()[0]
        item['cover'] = cover

        item['file_urls'] = 'http://www.95mm.com/slide-data/data/%s' % pid[0]
        item['item_cats'] = response.xpath('//div[@class="post-header"]/div[@class="post-info clearfix"]/span/a/text()').extract()[0].strip()
        item['item_tags'] = response.xpath('//span[@class="mod-tags"]/dl/dd/a/text()').extract()

        return item