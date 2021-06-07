# Std Libs:
import logging
# Django Libs:
from django.contrib.auth.models import User
from django.db.models import Q
# Django Rest Framework Libs:
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
# Locals:
from .models import Contract
from .permissions import ContractPermissions
from .serializer import ContractSerializer
from client.models import Client
from user.models import (SalerTHROUGH,
                         SupportTHROUGH)


logger = logging.getLogger(__name__)


class ContractCRUD(viewsets.ViewSet):
    """Contract management

    Generic argument:
        - client_id (int) : ID of the client
        - pk (int) : ID of the contract

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
            o create
            o retrieve
            o update
        Support :
            - list

    Generic Error:
        (HTTP status_code | detail)
        - 401 : JWT authentification failed
    """
    #permission_classes = (ContractPermissions)

    def list(self, request, client_id):
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
        # Check if client exist
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            content = {"detail": "Client doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        # Show all contracts from a client
        contracts = Contract.objects.all(client=client)
        
        serialized_contracts = ContractSerializer(contracts, many=True)

        if serialized_contracts.data:
            content = serialized_contracts.data
            return Response(data=content,
                            status=status.HTTP_200_OK)
        else:
            content = {"detail": "No contract available."}
            return Response(data=content,
                            status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, client_id, pk):
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
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            content = {"detail": "Client doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        try:
            contract = Contract.objects.get(Q(id=pk) &
                                            Q(client=client))
        except Contract.DoesNotExist:
            content = {"detail": "Contract Doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        serialized_contract = ContractSerializer(contract)
        if serialized_contract.data:
            content = serialized_contract.data
            # Check if user has permission to retrieve this client
            self.check_object_permissions(request, contract)
            return Response(data=content,
                            status=status.HTTP_200_OK)
        else:
            content = {"detail": "Contract details not available."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)

    def create(self, request, client_id):
        """
        POST request
        Method create

        Create a new client. Need to be connected to create one.

        Form:
            - status
            - amount
            - payment_due

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
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            content = {"detail": "Client doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        try:
            content = dict(request.data.items())
        except Exception:
            content = {"detail": "Form is invalid."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)
        if content:
            sales_contact = User.objects.get(id=request.user.id)
            try:
                content["sales_contact"] = sales_contact
                content["client"] = client
                contract = Contract(**content)
            except Exception:
                content = {"detail": "Form invalid."}
                logger.error(content.values())
                return Response(data=content,
                                status=status.HTTP_400_BAD_REQUEST)
            # Saving client
            contract.save()

            # Return client's data
            serialized_contract = ContractSerializer(contract)
            return Response(data=serialized_contract.data,
                            status=status.HTTP_201_CREATED)
        else:
            content = {"detail": "Form is empty."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, client_id, pk):
        """
        PUT request
        Method update

        Need to own the contract to update it.

        Form:
            - status
            - amount
            - payment_due

        Validate :
            (HTTP status_code | detail)
            - 200 : updated contract
        Errors :
            (HTTP status_code | detail)
            - 400 : Invalid form
            - 403 : Not permission to update
            - 404 : Element doesn't exist
        """
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            content = {"detail": "Client doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        try:
            contract_update = Contract.objects.get(Q(id=pk) &
                                                   Q(client=client))
        except Contract.DoesNotExist:
            content = {"detail": "Contract doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, contract_update)
        contract = Contract.objects.filter(id=pk)
        try:
            content = dict(request.data.items())
        except Exception:
            content = {"detail": "Form is invalid."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)
        if content:
            try:
                contract.update(**content)
            except Exception:
                content = {"detail": "Form is invalid."}
                logger.error(content.values())
                return Response(data=content,
                                status=status.HTTP_400_BAD_REQUEST)
            serialized_contract = ContractSerializer(contract, many=True)
            return Response(data=serialized_contract.data,
                            status=status.HTTP_200_OK)
        else:
            content = {"detail": "Empty form."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)