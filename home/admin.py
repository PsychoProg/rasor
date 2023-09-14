from django.contrib import admin
from . import models


@admin.register(models.ListBox)
class ListBoxAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'id']
    list_filter = ['created_at'] 
    search_fields = ['id', 'title']
    date_hierarchy = 'created_at'
    ordering = ['created_at']



@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'id']
    list_filter = ['created_at', 'tags'] 
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['id', 'title']
    date_hierarchy = 'created_at'
    ordering = ['created_at']


@admin.register(models.PageContent1)
class PageContent1Admin(admin.ModelAdmin):
    list_display = ['title', 'author']

@admin.register(models.PageContent2)
class PageContent2Admin(admin.ModelAdmin):
    list_display = ['title']
    

@admin.register(models.ShareLinks)
class ShareLinksAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']
    


admin.site.register(models.CompanyInfo)
admin.site.register(models.AboutUs)

