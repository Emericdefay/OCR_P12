# Std Libs:
import logging
# Django Libs:
from django.contrib.auth.models import User
from django.db.models import Q
# Django Rest Framework Libs:
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Locals:
from .models import Event
from .permissions import EventPermissions
from .serializer import EventSerializer
from client.models import Client
from contract.models import Contract
from user.models import Support, SupportTHROUGH


logger = logging.getLogger(__name__)


class EventCRUD(viewsets.ViewSet):
    """Event management

    Generic argument:
        - client_id (int) : ID of the client
        - contract_id (int) : ID of the contract
        - pk (int) : ID of the event

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
            o retrieve
        Support :
            - list
            o read
            o update

    Generic Error:
        (HTTP status_code | detail)
        - 401 : JWT authentification failed
    """
    permission_classes = [EventPermissions]

    def list(self, request, client_id, contract_id):
        """
        GET request
        Method list

        Show all events linked to the authenticated user

        Validate :
            (HTTP status_code | detail)
            - 200 : events' list
            - 204 : No event
        Errors :
            (HTTP status_code | detail)
            - 403 : Not permission to list
            - 404 : Element not found
        """
        # Check if client exists
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            content = {"detail": "Client doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        # Check if contract exists
        try:
            contract = Contract.objects.get(Q(id=contract_id) &
                                            Q(client=client))
        except Contract.DoesNotExist:
            content = {"detail": "Contract doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)

        # Show all Events from a client
        events = Event.objects.filter(Q(client=client) &
                                      Q(event_status=contract))

        serialized_events = EventSerializer(events, many=True)

        if serialized_events.data:
            content = serialized_events.data
            return Response(data=content,
                            status=status.HTTP_200_OK)
        else:
            content = {"detail": "No event available."}
            return Response(data=content,
                            status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, client_id, contract_id, pk):
        """
        GET request
        Method retrieve

        Get a specific event for the seller|support user.

        Validate :
            (HTTP status_code | detail)
            - 200 : retrieve event
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
            contract = Contract.objects.get(Q(id=contract_id) &
                                            Q(client=client))
        except Contract.DoesNotExist:
            content = {"detail": "Contract Doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        try:
            event = Event.objects.get(Q(id=pk) &
                                      Q(client=client) &
                                      Q(event_status=contract))
        except Event.DoesNotExist:
            content = {"detail": "Event doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        serialized_event = EventSerializer(event)
        if serialized_event.data:
            content = serialized_event.data
            # Check if user has permission to retrieve this event
            self.check_object_permissions(request, event)
            return Response(data=content,
                            status=status.HTTP_200_OK)
        else:
            content = {"detail": "Event details not available."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)

    def create(self, request, client_id, contract_id):
        """
        POST request
        Method create

        Create a new event. Need to be a connected saler to create one.

        Form:
            - support_contact
            - attendees
            - event_date
            - notes

        Validate :
            (HTTP status_code | detail)
            - 201 : created event
        Errors :
            (HTTP status_code | detail)
            - 400 : Invalid form
            - 403 : Not permission to create
            - 404 : Element not found
            - 406 : Support User not acceptable
            - 500 : Internal error when added support
        """
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            content = {"detail": "Client doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        try:
            contract = Contract.objects.get(Q(id=contract_id) &
                                            Q(client=client))
        except Contract.DoesNotExist:
            content = {"detail": "Contract doesn't exist."}
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
            try:
                username = content['support_contact']
                try:
                    support_user = User.objects.get(username=username)
                except User.DoesNotExist:
                    content = {"detail": "User doesn't exist."}
                    logger.error(content.values())
                    return Response(data=content,
                                    status=status.HTTP_400_BAD_REQUEST)
                # Check if support user has Support role
                check_is_support = Support.objects.filter(
                    user=support_user
                )
                if check_is_support:
                    content["client"] = client
                    content["event_status"] = contract
                    content['support_contact'] = support_user
                    event = Event(**content)
                else:
                    content = {"detail": "This user is not a support."}
                    logger.error(content.values())
                    return Response(data=content,
                                    status=status.HTTP_406_NOT_ACCEPTABLE)
            except Exception:
                content = {"detail": "Form invalid."}
                logger.error(content.values())
                return Response(data=content,
                                status=status.HTTP_400_BAD_REQUEST)
            # Saving event
            event.save()

            # ADMIN TASK : DEBUG OPTION
            # Add support
            # try:
                # support = dict()
                # support["user"] = support_user
                # support['client'] = client
                # support['event'] = event
                # contact = SupportTHROUGH(**support)
            # except Exception:
                # content = {"detail": "Support couldn't be added."}
                # logger.error(content.values())
                # return Response(data=content,
                                # status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # Saving support
            # contact.save()
            # END DEBUG

            # Return client's data
            serialized_event = EventSerializer(event)
            return Response(data=serialized_event.data,
                            status=status.HTTP_201_CREATED)
        else:
            content = {"detail": "Form is empty."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, client_id, contract_id, pk):
        """
        PUT request
        Method update

        Need to own the event to update it.

        Form:
            - support_contact
            - attendees
            - event_date
            - notes

        Validate :
            (HTTP status_code | detail)
            - 200 : updated event
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
            contract = Contract.objects.get(Q(id=contract_id) &
                                            Q(client=client))
        except Contract.DoesNotExist:
            content = {"detail": "Contract doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        try:
            event_update = Event.objects.get(Q(id=pk) &
                                             Q(client=client) &
                                             Q(event_status=contract))
        except Event.DoesNotExist:
            content = {"detail": "Event doesn't exist."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, event_update)
        event = Event.objects.filter(id=pk)
        try:
            content = dict(request.data.items())
        except Exception:
            content = {"detail": "Form is invalid."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)
        if content:
            if 'support_contact' in content:
                try:
                    event.update(**content)
                except Exception:
                    content = {"detail": "Form is invalid."}
                    logger.error(content.values())
                    return Response(data=content,
                                    status=status.HTTP_400_BAD_REQUEST)
                # ADMIN TASK : DEBUG OPTION
                # try:
                #     support_TH = SupportTHROUGH.objects.filter(event_id=pk)
                #     support = User.objects.get(id=content['support_contact'])
                #     support_TH.update(support)
                # except SupportTHROUGH.DoesNotExist:
                #     content = {"detail": "Support doesn't exist."}
                #     logger.error(content.values())
                #     return Response(data=content,
                #                     status=status)
                # except Exception:
                #     content = {"detail": "Internal Error."}
                #     logger.error(content.values())
                #     return Response(
                #         data=content,
                #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
                #         )
                # END DEBUG
                serialized_event = EventSerializer(event, many=True)
                return Response(data=serialized_event.data,
                                status=status.HTTP_200_OK)
            else:
                try:
                    event.update(**content)
                except Exception:
                    content = {"detail": "Form is invalid."}
                    logger.error(content.values())
                    return Response(data=content,
                                    status=status.HTTP_400_BAD_REQUEST)
                serialized_event = EventSerializer(event, many=True)
                return Response(data=serialized_event.data,
                                status=status.HTTP_200_OK)
        else:
            content = {"detail": "Empty form."}
            logger.error(content.values())
            return Response(data=content,
                            status=status.HTTP_400_BAD_REQUEST)
