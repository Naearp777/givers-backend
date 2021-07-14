

from rest_framework import serializers

from .models import interestedevents, requestevents
from events.serializers import EventSerializer
from customuser.serializers import UserSerializer


class requesteventSerializervolunteer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True,many=False)
    event=EventSerializer(read_only=True,many=False)
    class Meta:
        model=requestevents
        fields='__all__'

# class approvalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=requestevents
#         fields='__all__'
#         extra_kwargs = {'user': {'required': False},'event': {'required': False}}

class interestedSerializervolunteer(serializers.ModelSerializer):
    class Meta:
        model=interestedevents
        fields='__all__'