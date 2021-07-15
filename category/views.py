from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import EventCategory
from .serializers import EventCategorySerializer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def category_event(request):
    all_events=EventCategory.objects.all()
    serializer=EventCategorySerializer(all_events,many=True)
    return Response(serializer.data)
