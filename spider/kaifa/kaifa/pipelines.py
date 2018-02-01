# -*- coding: utf-8 -*-

import hashlib
import json
import os
import shutil
import urllib.request, urllib.parse, urllib.error

# from django.utils.encoding import from scrapy import log
from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from unidecode import unidecode

from service.frontend.models import Photo
from config.settings import MEDIA_ROOT
from service.category.models import Category, Tag
from slugify import slugify

from .settings import FILES_STORE, IMAGES_STORE


class KaifaPipeline(object):
    def process_item(self, item, spider):
        return item


class KaifaImagePipeline(ImagesPipeline):

    default_headers = {
        'referer': 'http://aimm.92kaifa.com/qingchun/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, headers=self.default_headers, dont_filter=True)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        
        if not image_paths:
            raise DropItem("Item contains no paths")

        # item['image_paths'] = image_paths
        photolist = []

        for paths in image_paths:
            photo = os.path.basename(paths)

            dst = os.path.join(MEDIA_ROOT, 'photo', photo[:2], photo[2:4], photo)
            src = os.path.join(IMAGES_STORE, paths)

            if os.path.exists(os.path.dirname(dst)) == False:
                os.makedirs(os.path.dirname(dst))

            shutil.copy(src, dst)
            print(dst)

            photolist.append('/media/photo/' + photo[:2] +'/'+ photo[2:4] +'/'+ photo)

        print(photolist)

        try:
            photo = Photo.objects.get(id=item.get('iid'))
            photo.photolist =  json.dumps(photolist)
            photo.save()

        except Exception as e:
            raise
  
        return item

class KaifaCoverPipeline(ImagesPipeline):

    default_headers = {
        'referer': 'http://aimm.92kaifa.com/qingchun/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        yield Request(item['cover'], headers=self.default_headers, dont_filter=True)

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

        print(item['cover'])

        return item

class KaifaTagsPipeline(object):

    def process_item(self, item, spider):

        print(item['item_tags'], item['title'])

        try:
            photo = Photo.objects.get(title = item['title'])
        except Exception as e:
            raise DropItem("Item contains no Photo")
            return item

        print(item['item_tags'])

        for t in item['item_tags']:
            try:
                default = {'title':t, 'slug': slugify(t)}
                tags, _ = Tag.objects.get_or_create(title = t, defaults = default)
                photo.tags.add(tags)
            except Exception as e:
                raise DropItem("Item contains no Tags")

        return item


class KaifaFilesPipeline(FilesPipeline):

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

        item['title']   = data['slide']['title']
        item['likes']   = data['slide']['like']
        item['created'] = data['slide']['createtime']

        if not data['images']:
            raise DropItem("Item contains no images")

        for i in data['images']:
            images.append(i['image_url'])

        item['image_urls'] = images
        item['photolist']  = json.dumps(images)
        item['status']     = 0
        item['count']      = len(images)

        try:
            Photo.objects.get(title = item['title']).delete()
        except Exception as e:
            pass

        photo = item.save()
        photo.tags.remove()

        try:
            if '模特' in item['item_cats']: 
                name = '模特'
                slug = 'mete'
            if '丝袜' in item['item_cats']: 
                name = '丝袜'
                slug = 'siwa'
            if '性感' in item['item_cats']: 
                name = '性感'
                slug = 'xinggan'
            if '明星' in item['item_cats']: 
                name = '明星'
                slug = 'mingxing'
            if '清纯' in item['item_cats']: 
                name = '清纯'
                slug = 'qingchun'
            if '网络' in item['item_cats']: 
                name = '网络'
                slug = 'wangluo'
            cat, _ = Category.objects.get_or_create(title=name, subtitle=item['item_cats'].strip(), slug=slug)
            photo.category_id = cat.pk
            photo.save()
            item['iid'] = photo.pk
        except Exception as e:
            print(e, item['item_cats'])

        for t in item['item_tags']:
            try:
                default = {'title':t, 'slug': (slugify(unidecode(t)))}
                tagset  = Tag.objects.get_or_create(title = t, defaults = default)

                photo.tags.add(tagset[0])
                cat.tag_set.add(tagset[0])

                default = tagset = None

            except Exception as e:
                pass

        cat   = None
        photo = None

        print(item['cover'])

        return item

    def parseJson(self, path):
        data = None

        try:
            file = open(os.path.join(FILES_STORE, path), 'r')
            data = file.read()
            file.close()
            data = data.strip().strip('var slide_data =').strip()
            data = json.loads(data)
        except Exception as e:
            raise e

        return data
