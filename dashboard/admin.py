from django.contrib import admin
from .models import Comments


@admin.register(Comments)
class CommectsAdmin(admin.ModelAdmin):
    list_display = ['subject', 'user']
    readonly_fields = ['user','subject', 'message']
    list_per_page = 10
    search_fields = ['user', 'subject']