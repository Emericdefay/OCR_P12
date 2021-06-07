# Django Libs:
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Locals:
from .models import (SalerTHROUGH,
                     SupportTHROUGH)


# Register user
class CustomUser(admin.ModelAdmin):
    """ """
    fieldsets = [
        ('Username', {'fields': ['username']}),
        ('First name', {'fields': ['first_name']}),
        ('Last name', {'fields': ['last_name']}),
        ('Email', {'fields': ['email']}),
        ('Password', {'fields': ['password']}),
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUser)
