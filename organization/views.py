from customuser.serializers import UserSerializer
from events.serializers import EventSerializer
from volunteer.models import requestevents
from .serializer import RequestFormSerializer, approvalSerializer, requestedSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AND, IsAuthenticated
from rest_framework.response import Response
from customuser.models import User
from events.models import Events
from .models import requestform
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showrequest(request, E_id, V_id):
    try:
        approval = requestevents.objects.filter(user_id=V_id, event_id=E_id)
        serializer = approvalSerializer(approval, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approval(request, E_id, V_id):
    print(request.data)
    try:
        approval = requestevents.objects.get(user_id=V_id, event_id=E_id)
        approval.approved = request.data['approved']
        approval.pending = request.data['pending']
        approval.save()
        serializer = approvalSerializer(approval, many=False)
        event = Events.objects.get(id=E_id)
        user = User.objects.get(id=V_id)
        user_name = UserSerializer(user, many=False)
        eventname = EventSerializer(event, many=False)
        if(serializer.data['approved'] == True):
            email_template = render_to_string('Approved.html', {
                                              "event": eventname.data['name'], "username": user_name.data['username']})
            sign_up = EmailMultiAlternatives(
                "Approved",
                "Approved",
                settings.EMAIL_HOST_USER,
                [user_name.data['email']],
            )
            sign_up.attach_alternative(email_template, 'text/html')
            sign_up.send()
        elif(serializer.data['approved'] == False):
            email_template = render_to_string('Rejected.html', {
                                              "event": eventname.data['name'], "username": user_name.data['username']})
            sign_up = EmailMultiAlternatives(
                "Rejected",
                "Rejected",
                settings.EMAIL_HOST_USER,
                [user_name.data['email']],
            )
            sign_up.attach_alternative(email_template, 'text/html')
            sign_up.send()

        return Response({"success": True})

    except requestevents.DoesNotExist:
        return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_requested(request, E_id):
    try:
        requested = requestevents.objects.filter(
            event_id=E_id, request_volunteer=True)
        serializer = requestedSerializer(requested, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def requestforms(request):
    data = request.data
    try:
        form = requestform.objects.create(
            event=Events.objects.get(id=data['id']),
            ques_1=data['ques_1'],
            ques_2=data['ques_2'],
            ques_3=data['ques_3'],
        )
        serializer = RequestFormSerializer(form, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'you have already updated the form'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getrequestedform(request, E_id):
    try:
        requestedform = requestform.objects.get(event_id=E_id)
        serializer = RequestFormSerializer(requestedform, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
