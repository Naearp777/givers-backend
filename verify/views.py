from customuser.serializers import UserSerializer

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
        user.reject = request.data['reject']
        user.save()
        serializer = UserSerializer(user, many=False)
        if(serializer.data['verify'] == True):
            email_template = render_to_string('verified.html', {
                                              "username": serializer.data['username']})
            sign_up = EmailMultiAlternatives(
                "Verified",
                "Verified",
                settings.EMAIL_HOST_USER,
                [serializer.data['email']],
            )
            sign_up.attach_alternative(email_template, 'text/html')
            sign_up.send()
            data = {"success": True}
            return Response(data)
        if(serializer.data['reject'] == True):
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
            data = {"success": True}
            return Response(data)
        data = {"success": True}
        return Response(data)
    except User.DoesNotExist:
        return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showverifyrequest(request):
    try:
        approval = User.objects.filter(
            verify=False, admin=False, staff=False, reject=False)
        serializer = UserSerializer(approval, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showalluser(request):
    try:
        user = User.objects.filter(admin=False, staff=False)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showspecificrequest(request, U_id):
    try:
        sp_user = User.objects.get(id=U_id)
        serializer = UserSerializer(sp_user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showallvolunteer(request):
    try:
        user = User.objects.filter(admin=False, staff=False, volunteer=True)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
