# -*- coding: utf-8 -*-
from django.apps import AppConfig


class CategoryConfig(AppConfig):
    name = 'service.category'
    verbose_name = u'相册分类'

    def ready(self):
        pass
