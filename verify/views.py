from customuser.serializers import UserSerializer
from volunteer.models import requestevents
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from customuser.models import User
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verification(request, U_id):
    try:
        user = User.objects.get(id=U_id)
        user.verify = request.data['verify']
        user.save()
        serializer = UserSerializer(user, many=False)
        if(serializer.data['verify'] == True):
            email_template = render_to_string('Verified.html', {
                                              "username": serializer.data['name']})
            sign_up = EmailMultiAlternatives(
                "Verified",
                "Verified",
                settings.EMAIL_HOST_USER,
                [serializer.data['email']],
            )
            sign_up.attach_alternative(email_template, 'text/html')
            sign_up.send()
        elif(serializer.data['verify'] == False):
            email_template = render_to_string('reject_user.html', {
                "username": serializer.data['username']})
            sign_up = EmailMultiAlternatives(
                "Rejected",
                "Rejected",
                settings.EMAIL_HOST_USER,
                [serializer.data['email']],
            )
            sign_up.attach_alternative(email_template, 'text/html')
            sign_up.send()

        return Response({"success": True})

    except requestevents.DoesNotExist:
        return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
