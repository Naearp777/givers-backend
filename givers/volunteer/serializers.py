from django.db.models import fields
from rest_framework import serializers

from .models import requestevents
from customuser.models import User




class requesteventSerializervolunteer(serializers.ModelSerializer):
    class Meta:
        model=requestevents
        fields=['user','event','description','interested','request_volunteer','user_details']

class approvalSerializer(serializers.ModelSerializer):
    class Meta:
        model=requestevents
        fields='__all__'
        extra_kwargs = {'user': {'required': False},'event': {'required': False}}