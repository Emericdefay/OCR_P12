from django.db import models


class SupportTHROUGH(models.Model):
    """ """
    user_id = models.IntegerField(
        null=False,
        blank=False)
    evend_id = models.IntegerField(
        null=False,
        blank=False)


class SalerTHROUGH(models.Model):
    """ """
    user_id = models.IntegerField(
        null=False,
        blank=False)
    client_id = models.IntegerField(
        null=False,
        blank=False)
