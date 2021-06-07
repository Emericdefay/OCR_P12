# Django REST Libs
from rest_framework import serializers

# Local Libs
from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    """
    Contract serializer
    Based on serializers.ModelSerializer
    """
    class Meta():
        model = Contract
        fields = "__all__"
