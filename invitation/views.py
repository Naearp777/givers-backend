from invitation.serializers import InvitationSerializer
from events.models import Events
from customuser.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Invitation
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings
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
            created_at=data['created_at'],
        )
        serializer = InvitationSerializer(invite, many=False)
        user = User.objects.get(id=U_id)
        email_template = render_to_string('invitation.html')
        invited = EmailMultiAlternatives(
            "You are invited",
            "You are invited",
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        invited.attach_alternative(email_template, 'text/html')
        invited.send()

        return Response(serializer.data)
    except:
        data = {'message': 'Invitation already exists'}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invite_display_id(request, U_id):
    invitation = Invitation.objects.filter(user_id=U_id)
    serializer = InvitationSerializer(invitation, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invite_display_id_read(request, I_id):
    invitation = Invitation.objects.get(id=I_id)
    invitation.read = True
    invitation.save()
    serializer = InvitationSerializer(invitation, many=False)
    return Response(serializer.data)
