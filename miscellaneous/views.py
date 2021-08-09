from typing import Counter
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from customuser.models import User
from events.models import Events
from volunteer.models import requestevents
from rest_framework import serializers, status
from events.serializers import EventSerializer
from customuser.serializers import UserSerializer
from volunteer.serializers import requesteventSerializervolunteer
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_specific_category(request, category_id):
    try:
        category = Events.objects.filter(category=category_id)
        serializer = EventSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_event_desc(request):
    try:
        category = Events.objects.order_by('-end_date')
        serializer = EventSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_event_postedtime(request):
    try:
        category = Events.objects.order_by('-posted_at')
        serializer = EventSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def searchevents(request):
    query = request.query_params.get('keyword')
    print('query:', query)
    if query == None:
        query = ''

    event = Events.objects.filter(name__icontains=query)
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def searchuser(request):
    query = request.query_params.get('keyword')
    print('query:', query)
    if query == None:
        query = ''

    users = User.objects.filter(username__icontains=query)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_number_approved_requested(request, E_id):
    try:
        approval_no = requestevents.objects.filter(
            event_id=E_id, approved=True).count()
        reviewed_no = requestevents.objects.filter(
            event_id=E_id, pending=False).count()
        requested_no = requestevents.objects.filter(
            event_id=E_id, request_volunteer=True).count()
        message = {"approval": approval_no,
                   "reviewed": reviewed_no, "requested": requested_no}
        return Response(message, status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
