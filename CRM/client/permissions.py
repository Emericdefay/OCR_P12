# Django Libs

# Django Rest Framework Libs:
from rest_framework import permissions
# Locals:
from .models import Client
from user.models import (SalerTHROUGH,
                           SupportTHROUGH)


class ClientPermissions(permissions.BasePermission):
    """ """
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True