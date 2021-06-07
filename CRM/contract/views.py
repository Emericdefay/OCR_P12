# Std Libs:

# Django Libs:

# Django Rest Framework Libs:
from rest_framework import viewsets
# Locals:
from .models import Contract
from .permissions import ContractPermissions

class ContractCRUD(viewsets.ViewSet):
    """ """
    permission_classes = (ContractPermissions)

    def list(self, request):
        """ """
        pass

    def retrieve(self, request, client_id):
        """ """
        pass

    def create(self, request):
        """ """
        pass

    def update(self, request, client_id):
        """ """
        pass