from django.contrib import admin
from .models import *


# Register your models here.


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
    list_display_links = ['id', 'name']


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
    list_display_links = ['id', 'name']


class GalleryInline(admin.TabularInline):
    fk_name = 'item'
    model = Gallery


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'material', 'collection', 'price']
    ordering = ['id']
    list_display_links = ['id', 'name']
    inlines = [GalleryInline, ]


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    ordering = ['id']
    list_display_links = ['id', 'title']


class CountBlogAboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    ordering = ['id']
    list_display_links = ['id', 'title']


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(CountBlogAbout, CountBlogAboutAdmin)
