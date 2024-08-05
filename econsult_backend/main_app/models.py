from datetime import timezone
from django.db import models

# Create your models here.

class StudentModel(models.Model):
    full_name = models.CharField(max_length=50)
    # date_of_birth = models.DateField()
    age = models.IntegerField()
    # gender = models.CharField(max_length=10)
    # spouse_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    # place_of_birth = models.CharField(max_length=50)
    # current_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)

    # # educational background
    # elementary_school_name = models.CharField(max_length=50)
    # elementary_school_date_of_enrollment = models.DateField()
    # elementary_school_date_of_graduation = models.DateField()
    # elementary_school_start_date = models.DateField()
    # elementary_school_end_date = models.DateField()


    # junior_high_school_name = models.CharField(max_length=50)
    # junior_high_school_date_of_enrollment = models.DateField()
    # junior_high_school_date_of_graduation = models.DateField()
    # junior_high_school_start_date = models.DateField()
    # junior_high_school_end_date = models.DateField()


    # high_school_name = models.CharField(max_length=50)
    # high_school_date_of_enrollment = models.DateField()
    # high_school_date_of_graduation = models.DateField()
    # high_school_start_date = models.DateField()
    # high_school_end_date = models.DateField()

    # vocational_school_name = models.CharField(max_length=50)
    # vocational_school_date_of_enrollment = models.DateField()
    # vocational_school_date_of_graduation = models.DateField()
    # vocational_school_start_date = models.DateField()
    # vocational_school_end_date = models.DateField()

    # university_name = models.CharField(max_length=50)
    # university_date_of_enrollment = models.DateField()
    # university_date_of_graduation = models.DateField()
    # university_start_date = models.DateField()
    # university_end_date = models.DateField()

    # #work history
    # name_of_company = models.CharField(max_length=50)
    # occupation = models.CharField(max_length=50)
    # date_of_entry = models.DateField()
    # date_of_retirement = models.DateField()




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