from invitation.serializers import InvitationSerializer
from events.models import Events
from customuser.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Invitation
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def invite(request, U_id, E_id):
    data = request.data
    try:
        invite = Invitation.objects.create(
            user=User.objects.get(id=U_id),
            event=Events.objects.get(id=E_id),
            description=data['description'],
            read=data['read'],
        )
        serializer = InvitationSerializer(invite, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Invitation already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invite_display_id(request, U_id):
    invitation = Invitation.objects.get(user_id=U_id)
    serializer = InvitationSerializer(invitation, many=False)
    return Response(serializer.data)
