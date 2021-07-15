from django.urls import path
from .import views

urlpatterns=[

    path('api/events_category/',views.category_event,name='event_category'),

]