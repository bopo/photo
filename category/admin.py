from category.models import Category, Tag
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'subtitle', 'parent', 'slug')
    # list_filter  = ('sites',)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)