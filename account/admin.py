from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Student


admin.site.register(Student)
admin.site.unregister(Group)
