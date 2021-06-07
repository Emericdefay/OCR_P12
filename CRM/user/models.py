# Django Libs:
from django.db import models
from django.contrib.auth.models import User
# Locals:
from client.models import Client
from event.models import Event


class Support(models.Model):
    """
    Support model

    Fields:
        - user
    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)


class SupportTHROUGH(models.Model):
    """
    SupportTHROUGH model

    Fields:
        - user
        - event
        - client
    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    event = models.ForeignKey(
        Event,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    client = models.ForeignKey(
        Client,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)


class Saler(models.Model):
    """
    Saler model

    Fields:
        - user
    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)


class SalerTHROUGH(models.Model):
    """
    SalerTHROUGH model

    Fields:
        - user
        - client
    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    client = models.ForeignKey(
        Client,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
