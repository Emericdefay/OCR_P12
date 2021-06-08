# Django Libs
from django.db.models import Q
# Django Rest Framework Libs:
from rest_framework import permissions
# Locals:
from user.models import (Saler,
                         SalerTHROUGH,
                         Support,
                         SupportTHROUGH)


class EventPermissions(permissions.BasePermission):
    """Events permissions

    Legend:
    A: All users (Saler & Support)
    1: Saler
    2: Support
    ': Meaning user is linked to the element.

        User permissions :
            A : list
            1': create
            A': retrieve
            2': update

        Object manipulation permissions :
            A': retrieve
            2': update
    """
    def has_permission(self, request, view):
        """
        User permissions :
            A : list
            1' : create
            A': retrieve
            2': update
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
            supports_th = SupportTHROUGH.objects.values()
            for support in list(supports_th):
                if request.user.id == support["user_id"]:
                    return True
        if view.action == 'update':
            supports_th = SupportTHROUGH.objects.values()
            for support in list(supports_th):
                if request.user.id == support["user_id"]:
                    return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Object manipulation permissions :
            A': retrieve
            2': update
        """
        if view.action == 'retrieve':
            user_id = request.user.id
            support_user = SupportTHROUGH.objects.filter(Q(user_id=user_id) &
                                                         Q(client_id=obj.id))
            saler_user = SalerTHROUGH.objects.filter(Q(user_id=user_id) &
                                                     Q(client_id=obj.id))
            if support_user or saler_user:
                return True
        if view.action == 'update':
            user_id = request.user.id
            support_user = SupportTHROUGH.objects.filter(Q(user_id=user_id) &
                                                         Q(client_id=obj.id))
            if support_user:
                return True
        return False
