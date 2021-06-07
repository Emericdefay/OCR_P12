# Std Libs:

# Django Libs:
from django.contrib.auth.models import User
from django.db.models import Q
# Django Rest Framework Libs:
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
# Locals:
from .models import Client
from .permissions import ClientPermissions
from .serializer import ClientSerializer


class ClientCRUD(viewsets.ViewSet):
    """Client management

    Generic argument:
        - client_id (int) : ID of the client

    Methods:
        - GET    : list
        - GET    : retrieve
        - POST   : create
        - PUT    : update

    Permissions:
        LEGEND: {
        '-': 'always permit',
        'o': 'need to be assignee',
        }
        Seller :
            - list
            - create
            o retrieve
            o update
        Support :
            - list
            o retrieve

    Generic Error:
        (HTTP status_code | detail)
        - 401 : JWT authentification failed
    """
    permission_classes = (ClientPermissions)

    def list(self, request):
        """
        GET request
        Method list

        Show all clients linked to the authenticated user

        Validate :
            (HTTP status_code | detail)
            - 200 : clients' list
            - 204 : No client
        Errors :
            (HTTP status_code | detail)
            - 403 : Not permission to list
        """
        # Show all clients
        clients = Client.objects.all()
        
        serialized_clients = ClientSerializer(clients, many=True)

        if serialized_clients.data:
            content = serialized_clients.data
            return Response(data=content,
                            status=status.HTTP_200_OK)
        else:
            content = {"detail": "No client available."}
            return Response(data=content,
                            status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, client_id):
        """
        GET request
        Method retrieve

        Get a specific client for the seller|support user.

        Validate :
            (HTTP status_code | detail)
            - 200 : retrieved client
        Errors :
            (HTTP status_code | detail)
            - 400 : Invalid form
            - 403 : Not permission to retrieve
            - 404 : Element doesn't exist
        """
        pass

    def create(self, request):
        """
        """
        pass

    def update(self, request, client_id):
        """
        """
        pass