# Django REST Libs
from rest_framework import serializers

# Local Libs
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Event serializer
    Based on serializers.ModelSerializer
    """
    class Meta():
        model = Event
        fields = "__all__"
