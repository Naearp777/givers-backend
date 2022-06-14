from django.urls import path
from .import views

urlpatterns=[

    path('approval/<int:E_id>/<int:V_id>/',views.approval,name='approval'),
    path('approval/request/<int:E_id>/<int:V_id>/',views.showrequest,name='show_request'),
    path('requested/<int:E_id>/',views.show_all_requested,name='all_request'),
    path('request/form/',views.requestforms,name='request_form'),
    path('requested/form/<int:E_id>/',views.getrequestedform,name='request_form'),
]