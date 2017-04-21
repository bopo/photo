# -*- coding: utf-8 -*-
# Scrapy settings for aimm project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))

BOT_NAME          = 'aimm'
SPIDER_MODULES    = ['aimm.spiders']
NEWSPIDER_MODULE  = 'aimm.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT        = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
COOKIES_ENABLED   = True
IMAGES_MIN_HEIGHT = 50
IMAGES_MIN_WIDTH  = 50
IMAGES_STORE      = 'stores/images'
FILES_STORE       = 'stores/files'
DOWNLOAD_TIMEOUT  = 1200
# ITEM_PIPELINES    = [
#	'aimm.pipelines.AimmImagesPipeline',
#	'aimm.pipelines.AimmFilesPipeline',
	# 'aimm.pipelines.AimmTagsPipeline',
# ]
#DOWNLOADER_MIDDLEWARES = {'aimm.middlewares.ProxyMiddleware': 543}

#sys.path.append(os.path.join(HERE,'../'))
# sys.path.append(os.path.join(HERE,'../../'))
#sys.path.append(os.path.join(HERE,'../../thirdparty'))

#sys.path.append('D:/tmp/photo')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.local'