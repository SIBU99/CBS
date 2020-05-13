from rest_framework.generics import(
#ListCreateAPIView,
RetrieveUpdateDestroyAPIView,
#RetrieveUpdateAPIView,
CreateAPIView,
#ListAPIView,
#RetrieveAPIView,
#UpdateAPIView,
#DestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from ..models import Student
from .serializers import StudentSerializer
from django.contrib.auth.models import User

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = []

class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = []

class Login(APIView):
    "this will create login for the Student"
    def post(self, request, format=None):
        "this will run ever the post is called"
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            username = username,
            password = password
            )
        if not user :
            msg = {
                "Error": "Enter The Correct Username and password"
            }
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
        else:
            student  = user.studAcc.all()[0]
            data = StudentSerializer(student)
            return Response(
                data.data,
                status = status.HTTP_201_CREATED
            )

class ChangeCreditial(APIView):
    "This will change the credential"
    def post(self, request, format=None):
        reg_no  = request.data.get("reg_no", None)
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        if not reg_no:
            msg = {
                "Error": "Provide A ID"
            }
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
        
        try:
            student = Student.objects.get(reg_no = reg_no)
        except:
            msg = {
                "Error": "Provide A ID"
            }
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
        
        acc = student.authAccount

        if username:
            acc.username = username
        if password:
            acc.set_password(password)
        
        acc.save()

        msg = {
                "Status": "Account Credential Are changed"
            }
            return Response(msg, status= status.HTTP_201_CREATED)