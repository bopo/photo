# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class FrontentConfig(AppConfig):
    name = 'service.frontend'
    verbose_name = u'相册管理'

    def ready(self):
        pass
