from .models import SchoolFormModel, StudentModel
from .serializer import SchoolFormSerializer, StudentSerializer
from rest_framework import generics, status
from rest_framework.response import Response 
import openpyxl
from rest_framework.views import APIView
from django.contrib.auth.models import User

class StudentListCreate(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class SchoolFormListCreate(generics.ListCreateAPIView):
    queryset = SchoolFormModel.objects.all()
    serializer_class = SchoolFormSerializer

class SchoolFormRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolFormModel.objects.all()
    serializer_class = SchoolFormSerializer

class SchoolFormFillUp(APIView):

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
