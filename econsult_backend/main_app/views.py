from .models import SchoolFormModel, StudentModel
from .serializer import SchoolFormSerializer, StudentSerializer
from rest_framework import generics, status
from rest_framework.response import Response 
import openpyxl
from rest_framework.views import APIView
from django.contrib.auth.models import User
import os
from django.conf import settings

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

        students = StudentModel.objects.all()
        file_name = SchoolFormModel.objects.get(id=2)
        file_path = os.path.join(settings.MEDIA_ROOT,str(file_name.file))
        wb = openpyxl.load_workbook(file_path)
        sheet = wb["Sheet1"]
        for student in students:
            sheet["B7"] = student.full_name
            sheet["F9"] = student.age
            sheet["B13"] = student.nationality

            save_file_path = f'{student.full_name}.xlsx'
            wb.save(save_file_path)
        return Response({"message":"Form submitted successfully."})