from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from . import models

admin.site.register(models.Profile)
admin.site.register(models.Student)
# admin.site.unregister(Group)
