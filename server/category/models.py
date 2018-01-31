# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
# from uuslug import uuslug
from django.utils import timezone

class Category(models.Model):
    """
    Category model to be used for categorization of content. Categories are
    high level constructs to be used for grouping and organizing content,
    thus creating a site's table of contents.
    """
    title = models.CharField(
        '分类标题',
        max_length=200,
        help_text='Short descriptive name for this category.',
    )

    subtitle = models.CharField(
        '副标题',
        max_length=200,
        blank=True,
        null=True,
        default='',
        help_text='Some titles may be the same and cause confusion in admin '
                  'UI. A subtitle makes a distinction.',
    )

    slug = models.SlugField(
        'slug',
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )

    parent = models.ForeignKey('self', null = True, blank = True, verbose_name = '隶属于')

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
        verbose_name = '类别'
        verbose_name_plural = '类别管理'

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

class Tag(models.Model):
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
        verbose_name = '标签'
        verbose_name_plural = '标签管理'
