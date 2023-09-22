from django.contrib import admin
from . import models


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'is_paid', 'created_at']
    inlines = [OrderItemAdmin]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'id']
    list_filter = ['status'] 
    search_fields = ['id', 'title']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'published_at'
    ordering = ['id']
    # autocomplete_fields = ['tags']
