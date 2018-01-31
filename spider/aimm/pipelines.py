# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy import log

from category.models import Category, Tag
from apps.models import Photo
from unidecode import unidecode

from .settings import FILES_STORE, IMAGES_STORE
from apps.settings import MEDIA_ROOT
import shutil, os, json, urllib.request, urllib.parse, urllib.error, hashlib

from django.utils.encoding import smart_unicode
from slugify import slugify


class AimmImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield Request(item['cover'])

    def item_completed(self, results, item, info):
        paths  = [x['path'] for ok, x in results if ok]

        if not paths:
            raise DropItem("Item contains no paths")

        cover = os.path.basename(paths[0])

        dst = os.path.join(MEDIA_ROOT, 'cover', cover[:2], cover[2:4], cover)
        src = os.path.join(IMAGES_STORE, paths[0])

        if os.path.exists(os.path.dirname(dst)) == False:
            os.makedirs(os.path.dirname(dst))

        shutil.move(src, dst)

        item['cover'] = 'cover/' + cover[:2] +'/'+ cover[2:4] +'/'+ cover

        print((item['cover']))

        return item

class AimmTagsPipeline(object):

    def process_item(self, item, spider):

        print(item['item_tags'], item['title'])

        try:
            photo = Photo.objects.get(title = item['title'])
        except Exception as e:
            raise DropItem("Item contains no Photo")
            return item

        print((item['item_tags']))

        for t in item['item_tags']:
            try:
                default = {'title':t, 'slug': smart_unicode(slugify(unidecode(t)))}
                tagset  = Tag.objects.get_or_create(title = t, defaults = default)
                photo.tags.add(tagset[0])
            except Exception as e:
                raise DropItem("Item contains no Tags")

        return item


class AimmFilesPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        yield Request(item['file_urls'])

    def item_completed(self, results, item, info):
        images = []
        paths  = [x['path'] for ok, x in results if ok]

        if not paths:
            raise DropItem("Item contains no paths")

        data = self.parseJson(paths[0])

        if not data:
            raise DropItem("Item contains no json data.")

        item['title']    = data['slide']['title']
        item['likes']    = data['slide']['like']
        item['pub_date'] = data['slide']['createtime']

        if not data['images']:
            raise DropItem("Item contains no images")

        for i in data['images']:
            images.append(i['image_url'])

        item['photolist'] = json.dumps(images)
        item['status']    = 0
        item['count']     = len(images)

        try:
            Photo.objects.get(title = item['title']).delete()
        except Exception as e:
            pass

        photo = item.save()
        photo.tags.remove()

        try:
            if '模特' in item['item_cats']: name = '模特'
            if '丝袜' in item['item_cats']: name = '丝袜'
            if '性感' in item['item_cats']: name = '性感'
            if '明星' in item['item_cats']: name = '明星'
            if '清纯' in item['item_cats']: name = '清纯'
            if '网络' in item['item_cats']: name = '网络'
            cat = Category.objects.get(title = name)
            photo.category.add(cat)
        except Exception as e:
            print(e, item['item_cats'])

        for t in item['item_tags']:
            try:
                default = {'title':t, 'slug': smart_unicode(slugify(unidecode(t)))}
                tagset  = Tag.objects.get_or_create(title = t, defaults = default)

                photo.tags.add(tagset[0])
                cat.tag_set.add(tagset[0])

                default = tagset = None

            except Exception as e:
                pass

        cat   = None
        photo = None

        print((item['cover']))

        return item

    def parseJson(self, path):
        data = None

        try:
            file = open(os.path.join(FILES_STORE, path), 'r')
            data = file.read()
            file.close()
            data = data.strip('var slide_data = ').strip()
            data = json.loads(data)
        except Exception as e:
            raise e

        return data