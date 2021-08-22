
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import EventCategory,  Skills
from .serializers import EventCategorySerializer,  SkillSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_event(request):
    all_events = EventCategory.objects.all()
    serializer = EventCategorySerializer(all_events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def skills(request):
    all_ward = Skills.objects.all()
    serializer = SkillSerializer(all_ward, many=True)
    return Response(serializer.data)
