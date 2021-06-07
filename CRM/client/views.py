# Std Libs:
import logging
# Django Libs:
from django.contrib.auth.models import User
# from django.db.models import Q
# Django Rest Framework Libs:
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework import status
# Locals:
from .models import Client
from .permissions import ClientPermissions
from .serializer import ClientSerializer
from user.models import (SalerTHROUGH)



logger = logging.getLogger(__name__)


class ClientCRUD(viewsets.ViewSet):
    """Client management

    Generic argument:
        - pk (int) : ID of the client

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
    permission_classes = [ClientPermissions,]

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

    def retrieve(self, request, pk):
        """
        GET request
        Method retrieve

        Get a specific client for the seller|support user.

        Validate :
            (HTTP status_code | detail)
            - 200 : retrieve client
        Errors :
            (HTTP status_code | detail)
            - 403 : Not permission to retrieve
            - 404 : Element doesn't exist
        """
        try:
            client = Client.objects.get(id=pk)
        except Client.DoesNotExist:
            content = {"detail": "Client doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        serialized_client = ClientSerializer(client)
        if serialized_client.data:
            content = serialized_client.data
            # Check if user has permission to retrieve this client
            self.check_object_permissions(request, client)
            return Response(data=content,
                            status=status.HTTP_200_OK)
        else:
            content = {"detail": "Client details not available."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        POST request
        Method create

        Create a new client. Need to be connected to create one.

        Form:
            - first_name
            - last_name
            - email
            - phone
            - mobile
            - company_name

        Validate :
            (HTTP status_code | detail)
            - 201 : created client
        Errors :
            (HTTP status_code | detail)
            - 400 : Invalid form
            - 403 : Not permission to create
            - 500 : Internal error when added saler
        """
        try:
            content = dict(request.data.items())
        except Exception:
            content = {"detail": "Form is invalid."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)
        if content:
            sale_contact = User.objects.get(id=request.user.id)
            try:
                content["sales_contact"] = sale_contact
                client = Client(**content)
            except Exception:
                content = {"detail": "Form invalid."}
                logger.error(content.values())
                return Response(data=content,
                                status=status.HTTP_400_BAD_REQUEST)
            # Saving client
            client.save()
            # Create the saler through
            try:
                saler = dict()
                saler["user"] = sale_contact
                saler["client"] = client
                contact = SalerTHROUGH(**saler)
            except Exception:
                content = {"detail": "Saler couldn't be added."}
                logger.error(content.values())
                return Response(data=content,
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # Saving sale contact
            contact.save()
            # Return client's data
            serialized_client = ClientSerializer(client)
            return Response(data=serialized_client.data,
                            status=status.HTTP_201_CREATED)
        else:
            content = {"detail": "Form is empty."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """
        PUT request
        Method update

        Need to own the project to update it.

        Form:
            - first_name
            - last_name
            - email
            - phone
            - mobile
            - company_name

        Validate :
            (HTTP status_code | detail)
            - 200 : updated project
        Errors :
            (HTTP status_code | detail)
            - 400 : Invalid form
            - 403 : Not permission to update
            - 404 : Element doesn't exist
        """
        try:
            client_update = Client.objects.get(id=pk)
        except Client.DoesNotExist:
            content = {"detail": "Client doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, client_update)
        client = Client.objects.filter(id=pk)
        try:
            content = dict(request.data.items())
        except Exception:
            content = {"detail": "Form is invalid."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)
        if content:
            try:
                client.update(**content)
            except Exception:
                content = {"detail": "Form is invalid."}
                logger.error(content.values())
                return Response(data=content,
                                status=status.HTTP_400_BAD_REQUEST)
            serialized_client = ClientSerializer(client, many=True)
            return Response(data=serialized_client.data,
                            status=status.HTTP_200_OK)
        else:
            content = {"detail": "Empty form."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)
