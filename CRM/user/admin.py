# Django Libs:
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Locals:
from .models import (Saler,
                     Support)


# Register user
class CustomUser(UserAdmin):
    """
    Allow Admins to Create/Update/Delete Users.
    """
    fieldsets = [
        ('Username', {'fields': ['username']}),
        ('First name', {'fields': ['first_name']}),
        ('Last name', {'fields': ['last_name']}),
        ('Email', {'fields': ['email']}),
        ('Password', {'fields': ['password']}),
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUser)


# Set role to user
class Role(admin.ModelAdmin):
    """
    Allow Admins to Create/Update/Delete Saler/Support's roles.
    """
    fieldsets = [
        ('Username', {'fields': ['user']}),
    ]

admin.site.register(Saler, Role)
admin.site.register(Support, Role)
