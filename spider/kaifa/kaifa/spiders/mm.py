# -*- coding: utf-8 -*-
import scrapy
from kaifa.items import KaifaItem

class MmSpider(scrapy.Spider):
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
        urls = response.xpath('//div[@class="list-box"]/div[@class="preview"]/a')
        page = response.xpath('//div[@class="pages"]//li[@class="next"]/a')

        for url in urls:
            cover = url.xpath('img/@data-original').extract()[0].strip()
            cover = response.urljoin(cover)
            meta = {'cover':cover}
            
            url = url.xpath('@href').extract()[0]
            url = response.urljoin(url)
            yield scrapy.Request(url, meta=meta, callback=self.parseItem)

        for link in page:
            if link:
                url = link.xpath('@href').extract()[0].strip()
                url = response.urljoin(url)
                yield scrapy.Request(url, callback = self.parse)

    def parseItem(self, response):
        item = KaifaItem()
        meta = response.meta
        pid = response.xpath('//script').re(r'var pid="(\d+)";')

        item['title'] = response.xpath('//span[@id="d_picTit"]/text()').extract()[0]
        item['cover'] = meta['cover']

        item['file_urls'] = 'http://aim.92kaifa.com/e/extend/api.php?id=%s' % pid[0]
        item['item_cats'] = response.xpath('//div[@class="post-header"]/div[@class="post-info clearfix"]/span/a/text()').extract()[0].strip()
        item['item_tags'] = response.xpath('//span[@class="mod-tags"]/dl/dd/a/text()').extract()

        yield item