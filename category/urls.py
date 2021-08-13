from django.urls import path
from .import views

urlpatterns = [

    path('api/events_category/', views.category_event, name='event_category'),
    path('api/skills/', views.skills, name='skills'),


]
