# Django Libs:
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Locals:
from .models import (Saler,
                     SalerTHROUGH,
                     Support,
                     SupportTHROUGH)


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
        ('User', {'fields': ['user']}),
    ]


admin.site.register(Saler, Role)
admin.site.register(Support, Role)


# Set support users to event
class ContactSupport(admin.ModelAdmin):
    """
    Allow Admins to Create/Update/Delete Saler/Support's linked to event.
    """
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Client', {'fields': ['client']}),
        ('Event', {'fields': ['event']}),
    ]


admin.site.register(SupportTHROUGH, ContactSupport)


# Set sale users to client
class ContactSaler(admin.ModelAdmin):
    """
    Allow Admins to Create/Update/Delete Saler/Support's linked to client.
    """
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Client', {'fields': ['client']}),
    ]


admin.site.register(SalerTHROUGH, ContactSaler)
