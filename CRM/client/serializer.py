# Django REST Libs
from rest_framework import serializers

# Local Libs
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """
    Client serializer
    Based on serializers.ModelSerializer
    """
    class Meta():
        model = Client
        fields = "__all__"
