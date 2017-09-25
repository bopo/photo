# -*- coding: utf-8 -*-
from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, ModelForm, Textarea, Select

# from suit_ckeditor.widgets import CKEditorWidget
# from suit_redactor.widgets import RedactorWidget

from suit.admin import SortableTabularInline, SortableModelAdmin
from suit.widgets import NumberInput, SuitDateWidget, SuitSplitDateTimeWidget, EnclosedInput, LinkedSelect, AutosizedTextarea
# from reversion import VersionAdmin
from suit.admin import SortableModelAdmin
from .models import Photo, Weblink, Notice, Category,Tags

def published(modeladmin, request, queryset):
    queryset.update(status=1)


def recommend(modeladmin, request, queryset):
    queryset.update(recommend=1)

published.short_description = u"发布所选的项目"
recommend.short_description = u"推荐所选的项目"


class PhotoForm(ModelForm):
    class Meta:
        widgets = {
            'count': NumberInput(attrs={'class': 'input-mini'}),
            'ordering': NumberInput(attrs={'class': 'input-mini'}),
        }

# class PhotoAdmin(ModelAdmin):

#     def preview(self, obj):
#         return '<img src="%s" height="64" width="64" />' % (obj.cover)

#     actions = [published, recommend]
#     list_display = ('title', 'views', 'likes', 'count', 'pub_date', 'recommend', 'status')
#     search_fields = ('title', 'pub_date')
#     # list_filter   = ('id', 'title', 'views')

#     preview.allow_tags = True
#     preview.short_description = u'图片'

class PhotoInline(admin.TabularInline):
    model = Photo
    suit_classes = 'suit-tab suit-tab-cities'

class TabbedPhotoAdmin(ModelAdmin):
    # inlines = (PhotoInline,)

    def preview(self, obj):
        return '<img src="%s" height="64" width="64" />' % (obj.cover)

    sortable = 'ordering'
    form = PhotoForm
    actions = [published, recommend]

    list_display = ('title', 'views', 'likes', 'count', 'pub_date', 'recommend', 'status')
    search_fields = ('title', 'pub_date')

    def suit_row_attributes(self, obj, request):
        css_class = {
            1: 'success',
            0: 'warning',
            -1: 'error',
        }.get(obj.status)

        if css_class:
            return {'class': css_class, 'data': obj.title}

    def suit_cell_attributes(self, obj, column):
        if column == 'status' or column == 'recommend':
            return {'class': 'text-center'}
        elif column == 'status':
            return {'class': 'text-error'}

    # Or bit more advanced example
    def suit_row_attributes(self, obj, request):

        css_class = {1: 'success', 0: 'warning', -1: 'error', }.get(obj.status)

        if css_class:
            return {'class': css_class, 'data': obj.title}


    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['title', 'slug', 'cover', 'photolist', 'category', 'tags']
        }),
        (None, {
            'classes': ('suit-tab suit-tab-info',),
            'fields': ['views', 'likes','count','ordering', 'recommend', 'status']}
        ),
    ]

    suit_form_tabs = (('general', u'基本'), ('info', u'扩展'))
    suit_form_includes = None

# class NoticeAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'pub_date')


class WeblinkAdmin(ModelAdmin):
    list_display = ('name', 'icon', 'url')
    search_fields = ('name', 'url')


# class TabbedPhotoAdmin(PhotoAdmin):
#     # list_filter = ('id', 'title', 'views')
#     suit_form_tabs = (('tab1', u'基本'), ('tab2', u'扩展'))
#     suit_form_includes = None


class NoticeForm(ModelForm):
    class Meta:
        # model = Notice
        widgets = {
            # 'content': RedactorWidget(editor_options = {'autoresize': True}),
            # 'content': RedactorWidget,
            # 'content': RedactorWidget(editor_options={'buttons': ['html', '|', 'formatting', '|', 'bold', 'italic']}),
            # 'content': CKEditorWidget(editor_options=_ck_editor_config),
        }

class NoticeAdmin(ModelAdmin):
    form = NoticeForm
    search_fields = ('subject','pub_date',)
    list_display = ('subject','pub_date',)

    fieldsets = [
        (None, {'fields': ['subject']}),
        ('Content', {'classes': ('full-width',),'description': 'Full width example', 'fields': ('content',)})
    ]

class CategoryAdmin(ModelAdmin):
    list_display = ('title','subtitle')

admin.site.register(Tags)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Weblink, WeblinkAdmin)
admin.site.register(Photo, TabbedPhotoAdmin)
