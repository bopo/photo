# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Short descriptive name for this category.', max_length=200, verbose_name='分类标题')),
                ('subtitle', models.CharField(blank=True, default='', help_text='Some titles may be the same and cause confusion in admin UI. A subtitle makes a distinction.', max_length=200, null=True, verbose_name='副标题')),
                ('slug', models.SlugField(help_text='Short descriptive unique name for use in urls.', max_length=255, unique=True, verbose_name='slug')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Category', verbose_name='隶属于')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别管理',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Short descriptive name for this tag.', max_length=200)),
                ('slug', models.SlugField(help_text='Short descriptive unique name for use in urls.', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签管理',
            },
        ),
    ]
