from django.urls import path
from .import views

urlpatterns = [

    path('api/request_event/<int:V_id>/<int:E_id>/',
         views.requestevent, name='request_event'),
    path('api/interested/event/', views.interestedevent, name='interested_event'),
    path('api/interested/<int:V_id>/', views.showinterested, name='interested'),
    path('api/requested_specific/<int:V_id>/', views.show_requested_specific_user, name='requested_specific_user'),

]
