from django.contrib import admin
from .models import Product, Cart


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at', 'id']
    # list_filter = ['status', 'created_at', 'published_at', 'author'] 
    search_fields = ['id', 'name']
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'published_at'
    ordering = ['id']
    # autocomplete_fields = ['tags']

admin.site.register(Cart)