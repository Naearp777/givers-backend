from events.serializers import EventSerializer, UserSerializer
from invitation.models import Invitation
from rest_framework import serializers


class InvitationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    event = EventSerializer(read_only=True, many=False)
    class Meta:
        model = Invitation
        fields='__all__'
