from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'username', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']

    class Meta:
        managed = True



# admin.site.register(User, UserAdmin)

# admin.site.unregister(Group)
