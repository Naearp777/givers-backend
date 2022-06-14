from django.urls import path
from .import views

urlpatterns = [

    path('events/sort/<int:category_id>/',
         views.show_specific_category, name='sort_category'),
    path('events/sort_desc/', views.show_event_desc, name='show_event_desc'),
    path('events/', views.show_event_postedtime, name='show_posted_latest'),
    path('events/search/', views.searchevents, name='search_event'),
    path('users/search/', views.searchuser, name='search_user'),
    path('show/number/<int:E_id>/',
         views.show_number_approved_requested, name='approval_no'),
    path('skills/search/<str:skill>',
         views.search_by_skills, name='search_skills'),
    path('advance_search/',
         views.advance_search.as_view(), name='advance_search'),
]
