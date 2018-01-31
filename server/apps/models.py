# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from .settings import MEDIA_ROOT, THUMB_ROOT, MEDIA_URL
# from ckeditor.fields import RichTextField
# from social.models import AbstractBaseSiteUser, AbstractInnerUserAuth, AbstractUserInfo

import datetime


class Photo(models.Model):
    title = models.CharField('相册标题', max_length=64)
    slug = models.CharField('相册标示', max_length=64)
    cover = models.ImageField('封面相册', upload_to='cover/', blank=False)
    photolist = models.TextField(verbose_name='图片列表', default='')
    views = models.IntegerField('浏览数', default=0)
    likes = models.IntegerField('喜欢数', default=0)
    count = models.IntegerField('相册数', default=0)
    pub_date = models.DateTimeField('发布时间', auto_now=True)
    ordering = models.IntegerField('排序', default=9999)
    recommend = models.BooleanField('推荐', default=0)
    category = models.ManyToManyField('category.Category')
    tags = models.ManyToManyField('category.Tag')
    status = models.BooleanField(verbose_name='发布状态', default=False)
    # status    = models.PositiveSmallIntegerField(
    #     choices = ((0, u'未发布'), (1, u'已发布')),
    #     verbose_name = u'状态',
    # )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/detail/%s/" % self.id

    class Meta:
        verbose_name = '相册'
        verbose_name_plural = '相册管理'
        # app_label = u"我的应用"
        # db_table = 'apps_photo'

from django.utils import timezone

class Weblink(models.Model):
    name = models.CharField('网站名称', max_length=64)
    icon = models.URLField('网站图标', max_length=100)
    url = models.URLField('网站URL', max_length=100)
    # pubdate = models.DateField(u'发布时间', default=timezone.now())

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
        # app_label = u"我的应用"
        # db_table = 'apps_weblink'


class Notice(models.Model):
    subject = models.CharField('公告标题',max_length=64)
    content = models.TextField('公告内容', blank=True)
    pub_date = models.DateTimeField('发布时间', auto_now=True)

    def __unicode__(self):
        return self.subject
        
    # class Meta:
    #     verbose_name = u'公告管理'
    #     verbose_name_plural = u'公告管理'
        # app_label = u"我的应用"
        # db_table = 'apps_notice'

# class UserAuth(AbstractInnerUserAuth):
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=128)

# class UserInfo(AbstractUserInfo):
#     pass
