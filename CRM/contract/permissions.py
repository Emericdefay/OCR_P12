# Django Libs
from django.db.models import Q
# Django Rest Framework Libs:
from rest_framework import permissions
# Locals:
from user.models import (Saler,
                         SalerTHROUGH,
                         Support)


class ContractPermissions(permissions.BasePermission):
    """Contracts permissions

    Legend:
    A: All users (Saler & Support)
    1: Saler
    2: Support
    ': Meaning user is linked to the element.

        User permissions :
            A : list
            1': create
            1': retrieve
            1': update

        Object manipulation permissions :
            1': retrieve
            1': update
    """
    def has_permission(self, request, view):
        """
        User permissions :
            A : list
            1' : create
            1': retrieve
            1': update
        """
        if not request.user.is_authenticated:
            return False
        if view.action == 'list':
            salers = Saler.objects.values()
            for saler in list(salers):
                if request.user.id == saler["user_id"]:
                    return True
            supports = Support.objects.values()
            for support in list(supports):
                if request.user.id == support["user_id"]:
                    return True
        if view.action == 'create':
            salers_th = SalerTHROUGH.objects.values()
            for saler in list(salers_th):
                if request.user.id == saler["user_id"]:
                    return True
        if view.action == 'retrieve':
            salers_th = SalerTHROUGH.objects.values()
            for saler in list(salers_th):
                if request.user.id == saler["user_id"]:
                    return True
        if view.action == 'update':
            salers_th = SalerTHROUGH.objects.values()
            for saler in list(salers_th):
                if request.user.id == saler["user_id"]:
                    return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Object manipulation permissions :
            1': retrieve
            1': update
        """
        if view.action == 'retrieve':
            user_id = request.user.id
            saler_user = SalerTHROUGH.objects.filter(Q(user_id=user_id) &
                                                     Q(client_id=obj.id))
            if saler_user:
                return True
        if view.action == 'update':
            user_id = request.user.id
            saler_user = SalerTHROUGH.objects.filter(Q(user_id=user_id) &
                                                     Q(client_id=obj.id))
            if saler_user:
                return True
        return False
