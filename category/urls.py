from django.urls import path
from .import views

urlpatterns = [

    path('api/events_category/', views.category_event, name='event_category'),
    path('api/country/', views.country, name='country'),
    path('api/province/', views.province, name='province'),
    path('api/district/', views.district, name='district'),
    path('api/municipality/', views.municipality, name='municipality'),
    path('api/ward/', views.ward, name='ward'),
    path('api/skills/', views.Skills, name='skills'),


]
