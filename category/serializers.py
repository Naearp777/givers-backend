from rest_framework import serializers
from .models import EventCategory

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=EventCategory
        fields='__all__'
