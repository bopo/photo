from django.conf.urls.defaults import *
from . import admin_views

urlpatterns = (
    (r'^tree/$', admin_views.tree),
)
