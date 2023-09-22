from django.contrib import admin
from .models import Comments, Course, CourseContent, CourseMessage, CourseRegistered


@admin.register(Comments)
class CommectsAdmin(admin.ModelAdmin):
    list_display = ['subject', 'user']
    readonly_fields = ['user','subject', 'message']
    list_per_page = 10
    search_fields = ['user', 'subject']


@admin.register(CourseContent)
class CourseContentAdmin(admin.ModelAdmin):
    list_display = ['course', 'title', 'created_at']
    list_per_page = 20
    search_fields = ['course', 'title']
    list_filter = ['course']
admin.site.register(Course)
admin.site.register(CourseMessage)

admin.site.register(CourseRegistered)