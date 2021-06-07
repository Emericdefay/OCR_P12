# Django Libs:
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Locals:
from .models import Event


# Register event
class CustomEvent(admin.ModelAdmin):
    """ """
    fieldsets = [
        ('Client', {'fields': ['client']}),
        ('support_contact', {'fields': ['support_contact']}),
        ('event_status', {'fields': ['event_status']}),
        ('attendees', {'fields': ['attendees']}),
        ('event_date', {'fields': ['event_date']}),
        ('notes', {'fields': ['notes']}),
    ]


admin.site.register(Event, CustomEvent)
