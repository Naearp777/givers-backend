from django.urls import path
from .import views

urlpatterns = [
     # For listing all events in ascending order of date
    path('events_ascending/', views.Event_display_all, name='all_events'),
    # For Displaying Event of ceratin id
    path('<int:E_id>/', views.Event_display_id, name='events_id'),
    # display the incomplete events of specific user, here E_id = user_id
    path('user/<int:user_id>/',
         views.Event_display_specific, name='events_specific'),
    path('history/<int:E_id>/',
         views.Event_display_completed, name='events_history'),
    path('register/', views.registerEvent, name='register_events'),
    path('update/<int:pk>/',
         views.EventUpdate.as_view(), name='update_events'),
]
