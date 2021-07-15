from django.urls import path
from .import views

urlpatterns=[

    path('api/approval/<int:E_id>/<int:V_id>/',views.approval,name='approval'),
    path('api/approval/request/<int:E_id>/<int:V_id>/',views.showrequest,name='show_request'),
    # path('api/requested/<int:E_id>/',views.show_all_requested,name='all_request'),
    path('api/update_request_api/<int:E_id>/',views.update_request_api,name='update_request_api'),
    path('api/requested/<int:pk>/',views.UpdateRequestAPI.as_view(),name='update-request'),
] 