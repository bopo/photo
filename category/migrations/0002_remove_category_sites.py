# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 02:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sites',
        ),
    ]
