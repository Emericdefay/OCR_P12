# Django Libs:
from django.db import models
from django.contrib.auth.models import User
# Locals:
from client.models import Client
from contract.models import Contract


class Event(models.Model):
    """Event model
    
    Fields:
        - client
        - date_created
        - date_updated
        - support_contact
        - event_status
        - attendees
        - event_date
        - notes
    """
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=False)
    date_created = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False)
    date_updated = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False)
    support_contact = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False)
    event_status = models.ForeignKey(
        Contract,
        on_delete=models.SET_NULL,
        null=True,
        blank=False)
    attendees = models.IntegerField(
        null=False,
        blank=False)
    event_date = models.DateTimeField(
        null=False,
        blank=False)
    notes = models.TextField(
        null=False,
        blank=False)
