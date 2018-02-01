# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime


class Photo(models.Model):
    title = models.CharField('相册标题', max_length=64)
    slug = models.CharField('相册标示', max_length=64)
    cover = models.ImageField('封面相册', upload_to='cover/', blank=False)
    photolist = models.TextField(verbose_name='图片列表', default='')
    views = models.IntegerField('浏览数', default=0)
    likes = models.IntegerField('喜欢数', default=0)
    count = models.IntegerField('相册数', default=0)
    created = models.DateTimeField('发布时间', auto_now=True)
    ordering = models.IntegerField('排序', default=9999)
    recommend = models.BooleanField('推荐', default=0)
    category = models.ForeignKey('category.Category', verbose_name='图片类别', blank=True, null=True)
    tags = models.ManyToManyField('category.Tag', verbose_name='图片标签', blank=True, null=True)
    status = models.BooleanField(verbose_name='发布状态', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/detail/%s/" % self.id

    class Meta:
        verbose_name = '相册'
        verbose_name_plural = '相册管理'
        # app_label = u"我的应用"
        # db_table = 'apps_photo'



class Weblink(models.Model):
    name = models.CharField('网站名称', max_length=100)
    logo = models.URLField('网站图标', max_length=200)
    link = models.URLField('网站URL', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
        # app_label = u"我的应用"
        # db_table = 'apps_weblink'


class Notice(models.Model):
    subject = models.CharField('公告标题',max_length=64)
    content = models.TextField('公告内容', blank=True)
    created = models.DateTimeField('发布时间', auto_now=True)

    def __str__(self):
        return self.subject
        
    class Meta:
        verbose_name = u'公告管理'
        verbose_name_plural = u'公告管理'
        # app_label = u"我的应用"
        # db_table = 'apps_notice'

