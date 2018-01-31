# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy import log

from aimm.items import AimmItem
from pprint import pprint
from os import path
import json, urllib.request, urllib.parse, urllib.error
# http://aim.92kaifa.com/e/extend/api.php?id=5368
# response.xpath('//div[@class="mod-channel"]/div[@class="channel-ctn"]')[0].xpath('//div[@class="list-box"]/div[@class="preview"]/a/img/@alt').extract(
# response.xpath('//div[@class="mod-channel"]/div[@class="channel-ctn"]')[0].xpath('//div[@class="list-box"]/div[@class="preview"]/div[@class="detail mt5"]/span/text()').extract()
# lb.xpath('//div[@class="pdw10"]/div[@class="tags"]/a/text()').extract()
# url = response.xpath('//li[@class="next"]/a/@href').extract()[0]
# p.xpath('span[@class="num"]/text()').extract()

class MmSpider(BaseSpider):
    name = 'mm'
    allowed_domains = ['aimm.92kaifa.com']
    start_urls = [
        'http://aimm.92kaifa.com/qingchun/',
        'http://aimm.92kaifa.com/mingxing/',
        'http://aimm.92kaifa.com/wangluo/',
        'http://aimm.92kaifa.com/xinggan/',
        'http://aimm.92kaifa.com/mote/',
        'http://aimm.92kaifa.com/siwa/',
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

        item['file_urls'] = 'http://aim.92kaifa.com/e/extend/api.php?id=%s' % pid[0]
        item['item_cats'] = sel.select('//div[@class="post-header"]/div[@class="post-info clearfix"]/span/a/text()').extract()[0].strip()
        item['item_tags'] = sel.select('//span[@class="mod-tags"]/dl/dd/a/text()').extract()

        return item