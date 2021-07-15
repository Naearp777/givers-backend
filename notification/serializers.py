from rest_framework import serializers
from .models import Notification
from events.models import Request_as_Volunteer
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields ='__all__'

class Request_as_volunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request_as_Volunteer
        fields ='__all__'