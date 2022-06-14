from django.urls import path
from .import views

urlpatterns = [

    path('events_category/', views.category_event, name='event_category'),
    path('skills/', views.skills, name='skills'),
]
