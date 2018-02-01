# -*- coding: utf-8 -*-
# Django settings for testproject project.
import os
import sys
HERE = os.path.dirname(__file__)
# ASSETS = os.path.join(HERE, 'assets')

ALLOWED_HOSTS = ('*')

DEBUG = True
# TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(HERE, '..', '..', 'sqlite3.db'),
        # 'NAME': 'django',
        # 'USER': 'root',
        # 'PASSWORD': '123',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        # 'DEFAULT_CHARSET': 'utf8',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(HERE, 'runtime/_cache'),
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'locmem:///',
        'TIMEOUT': 60,
    },
    'redis': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '<host>:<port>',
        'OPTIONS': {'DB': 1, 'PASSWORD': 'yadayada', },
    },
}

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_ETAGS = True
SECRET_KEY = 'vaO4Y<g#YRWG8;Md8noiLp>.w(w~q_b=|1`?9<x>0KxA%UB!63'

TIME_ZONE = 'UTC'

USE_TZ = True

LANGUAGE_CODE = 'zh-hans'
DATETIME_FORMAT = 'Y-m-d H:i:s'
HEADER_DATE_FORMAT = 'Y-m-d H:i:s'

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    # 'django.middleware.cache.CacheMiddleware',
    # 'django.middleware.doc.XViewMiddleware',
    # 'django.middleware.gzip.GZipMiddleware',

    # 'minidetector.Middleware',
)

# TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
#    os.path.join(HERE, 'templates_plus'),
#    os.path.join(HERE, 'templates'),
#)

ROOT_URLCONF = 'config.urls'
# TEMPLATE_DIRS = ()
INSTALLED_APPS = (
    'suit',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.admindocs',

        
    # 'mptt',
    'django_extensions',
    'service.frontend',
    'service.category',
    'easy_thumbnails',
    'suit_redactor',
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/'

STATIC_ROOT = os.path.join(HERE,  '../../assets', 'static')
THUMB_ROOT = os.path.join(HERE, '../../assets', 'media', 'thumb')
MEDIA_ROOT = os.path.join(HERE, '../../assets', 'media')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# STATICFILES_DIRS = (
#     os.path.join(HERE, "assets", 'static'),
# )


# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder"
# )
# Additional locations of static files
# STATICFILES_DIRS = (
#     os.path.join(STATIC_ROOT),
#     os.path.join(STATIC_ROOT, 'js'),
#     os.path.join(STATIC_ROOT, 'css'),
# )


# 333
# from django.conf.settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )

SUIT_CONFIG = {'ADMIN_NAME': '图片网站信息管理'}

ADMIN_MEDIA_PREFIX = '/media/'

# 333

THUMBNAIL_ALIASES = {
    '': {
        'thumb': {'size': (208, 291), 'crop': True},
        'rep': {'size': (254, 255), 'crop': True},
        'rep2': {'size': (203, 125), 'crop': True},
    },
}

TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        # 'DIRS': [],
        # 'APP_DIRS': True,
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

ALLOWED_HOSTS = ['*']
SITE_ID = 1

# SOCIAL_LOGIN_USER_INFO_MODEL='apps.UserInfo'
# SOCIALOAUTH_SITES = (
#     ('renren', 'socialoauth.sites.renren.RenRen', '人人',
#         {
#          'redirect_uri': 'http://test.codeshift.org/account/oauth/renren',
#          'client_id': 'YOUR ID',
#          'client_secret': 'YOUR SECRET',
#         }
#     ),
#     ('weibo', 'socialoauth.sites.weibo.Weibo', '新浪微博',
#         {
#           'redirect_uri': 'http://test.codeshift.org/account/oauth/weibo',
#           'client_id': 'YOUR ID',
#           'client_secret': 'YOUR SECRET',
#         }
#     ),
#     ('qq', 'socialoauth.sites.qq.QQ', 'QQ',
#         {
#           'redirect_uri': 'http://test.codeshift.org/account/oauth/qq',
#           'client_id': 'YOUR ID',
#           'client_secret': 'YOUR SECRET',
#         }
#     ),
#     ('douban', 'socialoauth.sites.douban.DouBan', '豆瓣',
#         {
#           'redirect_uri': 'http://test.codeshift.org/account/oauth/douban',
#           'client_id': 'YOUR ID',
#           'client_secret': 'YOUR SECRET',
#           'scope': ['douban_basic_common']
#         }
#     ),
# )
# 3
# try:
#     import gunicorn
#     INSTALLED_APPS += ('gunicorn',)
# except:
#     pass

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }

# 3

# 乱七八糟的配置，甭管具体是啥了，加上就是了，注意修改需要自定义的部分
# BROKER_URL = "amqp://root:toor@localhost:5672/rmq"
# CELERY_RESULT_BACKEND = "database"
# CELERY_RESULT_DBURI = "mysql://root:root@localhost/test"

# 把这两行放到 settings.py 文件尾
# import djcelery
# djcelery.setup_loader()

# rabbitmqctl set_permissions -p rmq root ".*" ".*" ".*"

# [program:celeryd]
# command = /usr/bin/python /var/www/photo/manage.py celeryd -B -E
# directory = /var/www/photo
# user = root
# autostart = true
# autorestart = true
# stdout_logfile = /var/log/supervisor/celeryd.log
# stderr_logfile = /var/log/supervisor/celeryd_err.log

# [program:celerycam]
# command = /usr/bin/python /var/www/photo/manage.py celerycam
# directory = /var/www/photo
# user = root
# autostart = true
# autorestart = true
# stdout_logfile = /var/log/supervisor/celerycam.log
# stderr_logfile = /var/log/supervisor/celerycam_err.log
