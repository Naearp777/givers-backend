from django.urls import path
from .import views

urlpatterns=[

    path('api/events/',views.Event_display_all,name='all_events'),
    path('api/events/<int:E_id>/',views.Event_display_id,name='events_id'),
    path('api/events/user/<str:username>/',views.Event_display_specific,name='events_specific'),
    # path('api/events/register/',views.registerEvent,name='register_events'),
    path('api/events/register/',views.RegisterEventAPI.as_view(),name='register_events'),


]