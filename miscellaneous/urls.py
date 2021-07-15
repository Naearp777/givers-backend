from django.urls import path
from .import views

urlpatterns=[

    path('api/events/sort/<int:category_id>/',views.show_specific_category,name='interested'),
    path('api/events/sort_desc/',views.show_event_desc,name='show_event_desc'),
]