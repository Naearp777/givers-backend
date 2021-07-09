from django.urls import path
from .import views

urlpatterns=[

    path('api/request_event/',views.requestevent,name='request_event'),
    # path('api/approval/<int:E_id>/<int:V_id>/',views.approval,name='approval'),
    # path('api/approval/request/<int:E_id>/<int:V_id>/',views.showrequest,name='show_request'),
    path('api/interested/<int:V_id>/',views.showinterested,name='interested'),
]