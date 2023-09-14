from django.contrib import admin
from . import models


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid', 'created_at']
    inlines = [OrderItemAdmin]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at', 'id']
    list_filter = ['status'] 
    search_fields = ['id', 'name']
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'published_at'
    ordering = ['id']
    # autocomplete_fields = ['tags']
