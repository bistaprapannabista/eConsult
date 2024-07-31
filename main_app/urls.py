from django.urls import path

from .views import SchoolFormFillUp, SchoolFormListCreate, SchoolFormRetrieveUpdateDestroy, StudentListCreate, StudentRetrieveUpdateDestroy

urlpatterns = [
    path('students', StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>', StudentRetrieveUpdateDestroy.as_view(), name='student-detail'),
    path('schoolforms', SchoolFormListCreate.as_view(), name='student-list-create'),
    path('schoolforms/<int:pk>', SchoolFormRetrieveUpdateDestroy.as_view(), name='student-detail'),
    path('fill-school-form',SchoolFormFillUp.as_view(),name="fill-school-form")
]