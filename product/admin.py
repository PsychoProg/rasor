from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    prepopulated_fields = { 'slug': ['title'] }
    list_per_page = 10
    search_fields = ['id', 'title']
    list_filter = ['updated_at']

