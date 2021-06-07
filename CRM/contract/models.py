# Django Libs:
from django.db import models
from django.contrib.auth.models import User
# Locals:
from client.models import Client


class Contract(models.Model):
    """ Contracts model

    Fields:
        - sales_contact
        - client
        - date_created
        - date_updated
        - status
        - amount
        - payment_due
    """
    sales_contact = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False)
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
    status = models.BooleanField(
        null=False,
        blank=False)
    amount = models.FloatField(
        null=False,
        blank=False)
    payment_due = models.DateTimeField(
        null=False,
        blank=False)
