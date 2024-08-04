from datetime import timezone
from django.db import models

# Create your models here.

class StudentModel(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.full_name + " - " + self.email
    

class SchoolFormModel(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100,null=True,blank=True)
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name =  'School Form'
        verbose_name_plural = 'School Forms'

    def __str__(self):
        return self.name