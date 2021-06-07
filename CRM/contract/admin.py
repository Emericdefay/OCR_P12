# Django Libs:
from django.contrib import admin
# Locals:
from .models import Contract


# Register contract
class CustomContract(admin.ModelAdmin):
    """
    Allow Admins to Create/Update/Delete Contracts.
    """
    fieldsets = [
        ('Client', {'fields': ['client']}),
        ('Sales contact', {'fields': ['sales_contact']}),
        ('Status', {'fields': ['status']}),
        ('Amount', {'fields': ['amount']}),
        ('Payment due', {'fields': ['payment_due']}),
    ]


admin.site.register(Contract, CustomContract)
