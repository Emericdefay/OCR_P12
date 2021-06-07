# Django Libs:
from django.contrib import admin
# Locals:
from .models import Client


# Register client
class CustomClient(admin.ModelAdmin):
    """
    Allow Admins to Create/Update/Delete Clients
    """
    fieldsets = [
        ('Sales contact', {'fields': ['sales_contact']}),
        ('First name', {'fields': ['first_name']}),
        ('Last name', {'fields': ['last_name']}),
        ('Email', {'fields': ['email']}),
        ('Phone', {'fields': ['phone']}),
        ('Mobile', {'fields': ['mobile']}),
        ('Company name', {'fields': ['company_name']}),
    ]


admin.site.register(Client, CustomClient)
