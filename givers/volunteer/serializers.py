from django.db.models import fields
from rest_framework import serializers

from .models import requestevents

class requesteventSerializervolunteer(serializers.ModelSerializer):
    class Meta:
        model=requestevents
        fields=['user','event','description','interested','request_volunteer','user_details']

class approvalSerializer(serializers.ModelSerializer):
    class Meta:
        model=requestevents
        fields='__all__'
    
    def update(self,instance,validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.event = validated_data.get('event', instance.event)
        instance.user_details = validated_data.get('user_details', instance.user_details)
        instance.description = validated_data.get('description', instance.description)
        instance.interested = validated_data.get('interested', instance.interested)
        instance.request_volunteer = validated_data.get('request_volunteer', instance.request_volunteer)
        instance.approved = validated_data.get('approved', instance.approved)

        instance.save()
        return instance