from django.db import models

from sis.models import *


from .randomm import create_new_ref_number


GENDER = [

      ('male', 'Male'),
      ('female', 'Female')

   ]
class Admission(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, blank=True)
    faculty = models.ForeignKey(to='sis.Faculty', related_name='adm_faculty', on_delete=models.CASCADE)
    dept = models.ForeignKey(to='sis.Department', related_name='adm_department', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='adm/images/')
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField()
    date_of_entry = models.DateField(default=timezone.now)
    # state_of_origin = models.
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
   
    # guardian information 

    fathter_name = models.CharField(max_length=50)
    father_phone = models.CharField(max_length=11)
    father_email = models.EmailField(blank=True)
    father_occupation = models.CharField(max_length=100)
    
    mother_name = models.CharField(max_length=50)
    mother_phone = models.CharField(max_length=11)
    mother_email = models.EmailField(blank=True)
    mother_occupation = models.CharField(max_length=100)

    registration_No= models.CharField(
           max_length = 11,
           blank=True,
           null=True,
           unique=True,
           default=create_new_ref_number()
      )

    def __str__(self):
        return str(self.registration_No)
        


  
    