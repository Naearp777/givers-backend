from django.urls import path
from .import views

urlpatterns=[

    path('api/events/sort/<int:category_id>/',views.show_specific_category,name='sort_category'),
    path('api/events/sort_desc/',views.show_event_desc,name='show_event_desc'),
    path('api/events/',views.show_event_postedtime,name='show_posted_latest'),
    path('api/events/search/',views.searchevents,name='search_event'),
    path('api/users/search/',views.searchuser,name='search_user'),
]