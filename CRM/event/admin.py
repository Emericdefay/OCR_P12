# Django Libs:
from django.contrib import admin
# Locals:
from .models import Event


# Register event
class CustomEvent(admin.ModelAdmin):
    """
    Allow Admins to Create/Update/Delete Events.
    """
    fieldsets = [
        ('Client', {'fields': ['client']}),
        ('support_contact', {'fields': ['support_contact']}),
        ('event_status', {'fields': ['event_status']}),
        ('attendees', {'fields': ['attendees']}),
        ('event_date', {'fields': ['event_date']}),
        ('notes', {'fields': ['notes']}),
    ]


admin.site.register(Event, CustomEvent)
