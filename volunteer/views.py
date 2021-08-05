
from .models import interestedevents, requestevents
from .serializers import interestedSerializervolunteer, requesteventSerializervolunteer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from customuser.models import User
from events.models import Events
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def requestevent(request, V_id, E_id):
    if requestevents.objects.filter(user_id=V_id, event_id=E_id).exists():
        message = {'message': 'You have already requested to this event'}
        return Response(message)
    else:
        data = request.data
        try:
            requestevent = requestevents.objects.create(
                user=User.objects.get(id=V_id),
                event=Events.objects.get(id=E_id),
                # description=data['description'],
                ques_1=data['ques_1'],
                ques_2=data['ques_2'],
                ques_3=data['ques_3'],
                ans_1=data['ans_1'],
                ans_2=data['ans_2'],
                ans_3=data['ans_3'],
                request_volunteer=data['request_volunteer'],
                approved=data['approved'],
                pending=data['pending'],
            )
            serializer = requesteventSerializervolunteer(
                requestevent, many=False)
            requestevent = requestevents.objects.get(id=serializer.data['id'])
            requestevent.user_details = request.FILES.get('user_details')
            requestevent.save()
            serializer = requesteventSerializervolunteer(
                requestevent, many=False)

            return Response(serializer.data)
        except:
            message = {
                'detail': 'requestevents with this content already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def showrequest(request,E_id,V_id):
#     try:
#         approval=requestevents.objects.filter(user_id=V_id ,event_id=E_id)
#         serializer=approvalSerializer(approval,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     except requestevents.DoesNotExist:
#          return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def approval(request,E_id,V_id):
#     try:
#         approval=requestevents.objects.get(user_id=V_id ,event_id=E_id)
#         serializer=approvalSerializer(approval,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data)
#         else:
#             return Response ({'status':'Failed'})
#     except requestevents.DoesNotExist:
#          return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showinterested(request, V_id):
    try:
        interested = interestedevents.objects.filter(
            user_id=V_id, interested=True)
        serializer = interestedSerializervolunteer(interested, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def interestedevent(request):
    data = request.data
    try:
        interested = interestedevents.objects.create(
            user=User.objects.get(username=data['username']),
            event=Events.objects.get(name=data['name']),
            interested=data['interested'],
        )
        serializer = requesteventSerializervolunteer(interested, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'You are already interested in this Event'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
