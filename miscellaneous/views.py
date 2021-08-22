from category.models import Skills

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from customuser.models import User
from events.models import Events
from volunteer.models import requestevents
from rest_framework import status
from events.serializers import EventSerializer
from customuser.serializers import UserSerializer
from category.serializers import SkillSerializer
from rest_framework.generics import ListAPIView
import django_filters
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_by_skills(request, skill):
    try:
        skills_get = Skills.objects.filter(skills=skill)
        serializer = SkillSerializer(skills_get, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Skills.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserFilter(django_filters.FilterSet):
    skills = django_filters.CharFilter(
        field_name='skills', lookup_expr='contains')
    age = django_filters.NumberFilter()
    age__gt = django_filters.NumberFilter(field_name='age', lookup_expr='gt')
    age__lt = django_filters.NumberFilter(field_name='age', lookup_expr='lt')

    class Meta:
        model = User
        fields = ['province', 'district', 'municipality', 'ward', ]


@permission_classes([IsAuthenticated])
class advance_search(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
