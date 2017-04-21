# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from .settings import MEDIA_ROOT, THUMB_ROOT, MEDIA_URL
# from ckeditor.fields import RichTextField
# from social.models import AbstractBaseSiteUser, AbstractInnerUserAuth, AbstractUserInfo

import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone

class Category(models.Model):
    """
    Category model to be used for categorization of content. Categories are
    high level constructs to be used for grouping and organizing content,
    thus creating a site's table of contents.
    """
    title = models.CharField(
        u'分类标题',
        max_length=200,
        help_text='Short descriptive name for this category.',
    )

    subtitle = models.CharField(
        u'副标题',
        max_length=200,
        blank=True,
        null=True,
        default='',
        help_text='Some titles may be the same and cause confusion in admin '
                  'UI. A subtitle makes a distinction.',
    )

    slug = models.SlugField(
        u'slug',
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )

    parent = models.ForeignKey('self', null = True, blank = True, verbose_name = u'隶属于')

    # sites = models.ManyToManyField(
    #     'sites.Site',
    #     blank = True,
    #     null = True,
    #     default='0',
    #     help_text='Limits category scope to selected sites.',
    #     verbose_name=u'站点',
    # )

    def __unicode__(self):
        return self.subtitle if self.subtitle else self.title

    class Meta:
        ordering = ('title',)
        verbose_name = u'类别'
        verbose_name_plural = u'类别管理'

    def save(self, *args, **kwargs):
        parent = self.parent

        while parent is not None:
            if parent == self:
                raise RuntimeError("Circular references not allowed")

            parent = parent.parent

        super(Category, self).save(*args, **kwargs)

    @property
    def children(self):
        return self.category_set.all().order_by('title')

    @property
    def tags(self):
        return Tag.objects.filter(categories__in=[self]).order_by('title')

    def get_absolute_url(self):
        return reverse('category_object_list', kwargs={'category_slug': self.slug})

class Tags(models.Model):
    """
    Tag model to be used for tagging content. Tags are to be used to describe
    your content in more detail, in essence providing keywords associated with
    your content. Tags can also be seen as micro-categorization of a site's
    content.
    """
    title = models.CharField(
        max_length=200,
        help_text='Short descriptive name for this tag.',
    )

    slug = models.SlugField(
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )

    # categories = models.ManyToManyField(
    #     Category,
    #     blank=True,
    #     null=True,
    #     help_text='Categories to which this tag belongs.'
    # )

    def __unicode__(self):
        return self.title

    # def save(self, *args, **kwargs):
        # self.slug = uuslug(self.title, instance=self)
        # super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签管理'

class Photo(models.Model):
    title = models.CharField(u'相册标题', max_length=64)
    slug = models.CharField(u'相册标示', max_length=64)
    cover = models.ImageField(u'封面相册', upload_to='cover/', blank=False)
    photolist = models.TextField(verbose_name=u'图片列表', default='')
    views = models.IntegerField(u'浏览数', default=0)
    likes = models.IntegerField(u'喜欢数', default=0)
    count = models.IntegerField(u'相册数', default=0)
    pub_date = models.DateTimeField(u'发布时间', auto_now=True)
    ordering = models.IntegerField(u'排序', default=9999)
    recommend = models.BooleanField(u'推荐', default=0)
    
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tags)
    
    status = models.BooleanField(verbose_name=u'发布状态', default=False)
    # status    = models.PositiveSmallIntegerField(
    #     choices = ((0, u'未发布'), (1, u'已发布')),
    #     verbose_name = u'状态',
    # )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/detail/%s/" % self.id

    class Meta:
        verbose_name = u'相册'
        verbose_name_plural = u'相册管理'
        # app_label = u"我的应用"
        # db_table = 'apps_photo'

# from django.utils import timezone

class Weblink(models.Model):
    name = models.CharField(u'网站名称', max_length=64)
    icon = models.URLField(u'网站图标', max_length=100)
    url = models.URLField(u'网站URL', max_length=100)
    # pubdate = models.DateField(u'发布时间', default=timezone.now())

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = u'友情链接'
        # app_label = u"我的应用"
        # db_table = 'apps_weblink'


class Notice(models.Model):
    subject = models.CharField(u'公告标题',max_length=64)
    content = models.TextField(u'公告内容', blank=True)
    pub_date = models.DateTimeField(u'发布时间', auto_now=True)

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
