from scrapy import log

import random

class ProxyMiddleware(object):
    proxy_list = []

    def __init__ (self):
        for p in open('proxy.txt'):
            p = p.strip().split(',')
            proxy = '%s://%s:%s/' % (p[0].lower(), p[1], p[2])
            self.proxy_list.append(proxy)

    def process_request(self, request, spider):

        try:
            proxy = random.choice(self.proxy_list)

            if proxy:
                request.meta['proxy'] = proxy
        except Exception,e:
            print 'proxy', e
            log.msg(e,level = log.ERROR)