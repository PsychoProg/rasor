from django.contrib import admin
from .models import ListBox, News 


@admin.register(ListBox)
class ListBoxAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'id']
    list_filter = ['created_at'] 
    search_fields = ['id', 'title']
    date_hierarchy = 'created_at'
    ordering = ['created_at']



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'id']
    list_filter = ['created_at', 'author'] 
    search_fields = ['id', 'title']
    date_hierarchy = 'created_at'
    ordering = ['created_at']

