from django.contrib import admin

from .models import SchoolFormModel, StudentModel

# Register your models here.


admin.site.register(StudentModel)
admin.site.register(SchoolFormModel)