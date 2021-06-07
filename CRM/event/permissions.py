# Django Libs

# Django Rest Framework Libs:
from rest_framework import permissions
# Locals:
from .models import Event
from client.models import Client
from contract.models import Contract
from user.models import (SalerTHROUGH,
                           SupportTHROUGH)


class EventPermissions(permissions.BasePermission):
    """ """
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)