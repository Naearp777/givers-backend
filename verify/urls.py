from django.urls import path
from .import views

urlpatterns = [

    path('api/verification/user/<int:U_id>/',
         views.verification, name='verification'),
    path('api/verification/alluser/',
         views.showverifyrequest, name='all_verify_list'),

]
