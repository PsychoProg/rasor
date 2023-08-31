from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'id']
    # list_filter = ['status', 'created_at', 'published_at', 'author'] 
    search_fields = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ['published_at', 'status']

