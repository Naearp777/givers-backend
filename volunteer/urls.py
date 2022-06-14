from django.urls import path
from .import views

urlpatterns = [

    path('request_event/<int:V_id>/<int:E_id>/',
         views.requestevent, name='request_event'),
    path('interested/event/', views.interestedevent, name='interested_event'),
    path('interested/<int:V_id>/', views.showinterested, name='interested'),
    path('requested_specific/<int:V_id>/', views.show_requested_specific_user, name='requested_specific_user'),
]
