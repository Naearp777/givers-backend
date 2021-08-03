from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import EventCategory
from .serializers import EventCategorySerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_event(request):
    all_events = EventCategory.objects.all()
    serializer = EventCategorySerializer(all_events, many=True)
    return Response(serializer.data)
