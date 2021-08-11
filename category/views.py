from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Country, District, EventCategory, Municipality, Province, Skills, Ward
from .serializers import CountrySerializer, DistrictSerializer, EventCategorySerializer, MunicipalitySerializer, ProvinceSerializer, SkillSerializer, WardSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_event(request):
    all_events = EventCategory.objects.all()
    serializer = EventCategorySerializer(all_events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def country(request):
    all_country = Country.objects.all()
    serializer = CountrySerializer(all_country, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def province(request):
    all_province = Province.objects.all()
    serializer = ProvinceSerializer(all_province, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def district(request):
    all_district = District.objects.all()
    serializer = DistrictSerializer(all_district, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def municipality(request):
    all_municipality = Municipality.objects.all()
    serializer = MunicipalitySerializer(all_municipality, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ward(request):
    all_ward = Ward.objects.all()
    serializer = WardSerializer(all_ward, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ward(request):
    all_ward = Skills.objects.all()
    serializer = SkillSerializer(all_ward, many=True)
    return Response(serializer.data)
