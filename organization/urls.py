from django.urls import path
from .import views

urlpatterns=[

    path('api/approval/<int:E_id>/<int:V_id>/',views.approval,name='approval'),
    path('api/approval/request/<int:E_id>/<int:V_id>/',views.showrequest,name='show_request'),
    path('api/requested/<int:E_id>/',views.show_all_requested,name='all_request'),
    path('api/request/form/',views.requestforms,name='request_form'),
    path('api/requested/form/<int:E_id>/',views.getrequestedform,name='request_form'),
]