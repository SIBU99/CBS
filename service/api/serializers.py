from rest_framework import serializers 
from ..models import Service

class ServiceSerializer(serializers.ModelSerializer):
    "This the serializer for the model : Service"
    class Meta:
        model = Service
        fields = [
            "bus_no",
            "startTime",
            "CurrentLocation",
            "option"
        ]