from datetime import datetime
from django.db import models

# Create your models here.

class StudentModel(models.Model):

    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    spouse_name = models.CharField(max_length=50,null=True)
    nationality = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=50,null=True)
    occupation = models.CharField(max_length=255,null=True)
    current_address = models.CharField(max_length=255,null=True)

    passport_number = models.CharField(max_length=20,null=True)
    passport_issue_date = models.DateField(null=True)
    passport_expire_date = models.DateField(null=True)


    # educational background
    elementary_school_name = models.CharField(max_length=50,null=True)
    elementary_school_date_of_enrollment = models.DateField(null=True)
    elementary_school_date_of_graduation = models.DateField(null=True)

    junior_high_school_name = models.CharField(max_length=50,null=True)
    junior_high_school_date_of_enrollment = models.DateField(null=True)
    junior_high_school_date_of_graduation = models.DateField(null=True)


    high_school_name = models.CharField(max_length=50,null=True)
    high_school_date_of_enrollment = models.DateField(null=True)
    high_school_date_of_graduation = models.DateField(null=True)

    vocational_school_name = models.CharField(max_length=50,null=True)
    vocational_school_date_of_enrollment = models.DateField(null=True)
    vocational_school_date_of_graduation = models.DateField(null=True)

    university_name = models.CharField(max_length=50,null=True)
    university_date_of_enrollment = models.DateField(null=True)
    university_date_of_graduation = models.DateField(null=True)

    #work history

    company_name1 = models.CharField(max_length=50,null=True)
    occupation1 = models.CharField(max_length=50,null=True)
    date_of_entry1 = models.DateField(null=True)
    date_of_retirement1 = models.DateField(null=True)

    company_name2 = models.CharField(max_length=50,null=True)
    occupation2 = models.CharField(max_length=50,null=True)
    date_of_entry2 = models.DateField(null=True)
    date_of_retirement2 = models.DateField(null=True)

    # #family member

    # father_name = models.CharField(max_length=50)
    # father_date_of_birth


    phone_number = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=255,null=True)
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