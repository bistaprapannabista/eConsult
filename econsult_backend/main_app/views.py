from datetime import datetime
from .models import SchoolFormModel, StudentModel
from .serializer import SchoolFormSerializer, StudentSerializer
from rest_framework import generics, status
from rest_framework.response import Response 
import openpyxl
from rest_framework.views import APIView
from django.contrib.auth.models import User
import os
from django.conf import settings
import json

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


def convert_to_numbers_list(arr):
    if not arr:
        return []
    
    comma_separated_string = arr[0]
    
    return [int(x) for x in comma_separated_string.split(',')]

class SchoolFormFillUp(APIView):

    def post(self, request, format=None):

        school_id = int(request.POST.get('school'))
        student_ids = convert_to_numbers_list([request.POST.get('students')])

        students = StudentModel.objects.filter(id__in=student_ids)
        file = SchoolFormModel.objects.get(id=school_id)

        documents_dir = os.path.join(settings.BASE_DIR, 'documents')
        os.makedirs(documents_dir, exist_ok=True)

        wb = openpyxl.load_workbook(file.file)

        sheet = wb["Sheet1"]
        for student in students:
            sheet["B7"] = student.full_name
            sheet["B9"] = student.date_of_birth
            sheet["B13"] = student.nationality
            sheet["H13"] = student.place_of_birth
            sheet["B15"] = student.current_address

            sheet["C24"] = student.elementary_school_name
            sheet["E24"] = student.elementary_school_date_of_enrollment
            sheet["G24"] = student.elementary_school_date_of_graduation

            sheet["C26"] = student.junior_high_school_name
            sheet["E26"] = student.junior_high_school_date_of_enrollment
            sheet["G26"] = student.junior_high_school_date_of_graduation

            sheet["C28"] = student.high_school_name
            sheet["E28"] = student.high_school_date_of_enrollment
            sheet["G28"] = student.high_school_date_of_graduation

            sheet["C30"] = student.vocational_school_name
            sheet["E30"] = student.vocational_school_date_of_enrollment
            sheet["G30"] = student.vocational_school_date_of_graduation

            sheet["C32"] = student.university_name
            sheet["E32"] = student.university_date_of_enrollment
            sheet["G32"] = student.university_date_of_graduation

            sheet["B43"] = student.company_name1
            sheet["D43"] = student.occupation1
            sheet["F43"] = student.date_of_entry1
            sheet["I43"] = student.date_of_retirement1


            sheet["B45"] = student.company_name2
            sheet["D45"] = student.occupation2
            sheet["F45"] = student.date_of_entry2
            sheet["I45"] = student.date_of_retirement2

            save_file_path = os.path.join(documents_dir, f'{student.full_name}-{file.name}-{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx')
            wb.save(save_file_path)
        return Response({"message":"Form submitted successfully."})