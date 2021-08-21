
from customuser.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(["GET"])
def validateusername(request, username):
    print(request)
    flag = 0
    if User.objects.filter(username=username):

        data = {"message": "Username already exists", "available": False}
        flag = 1
        return Response(data, status=status.HTTP_200_OK)

    elif flag == 0:
        data = {"message": "Available", "available": True}
        return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def validateemail(request, email):
    flag = 0

    if User.objects.filter(email=email):

        data = {"message": "Email already exists", "available": False}
        flag = 1
        return Response(data, status=status.HTTP_200_OK)

    elif flag == 0:
        data = {"message": "Available", "available": True}
        return Response(data, status=status.HTTP_200_OK)
