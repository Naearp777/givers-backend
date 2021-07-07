from django.urls import path
from .import views

urlpatterns=[

    path('api/request_event/',views.requestevent,name='request_event'),
    path('api/approval/<int:pk>/<int:pk1>/',views.ApprovalAPI.as_view(),name='approval'),

]