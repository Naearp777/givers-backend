from django.urls import path
from .import views

urlpatterns=[

    path('api/request_event/',views.requestevent,name='request_event'),
    path('api/approval/<int:E_id>/<int:V_id>/',views.approval,name='approval'),

]