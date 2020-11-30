from django.db import models

from sis.models import *


STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]

Marital_Status = [
    ('single', 'Single'),
    ('married', 'Married')
]


class Adm_Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='active')
    pin_number   = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='lecturer/images/')
    gender = models.CharField(max_length=10, choices=GENDER)
    marital_status = models.CharField(max_length=10, choices=Marital_Status)
    child = models.PositiveIntegerField()
    date_of_birth = models.DateField(default=timezone.now)
    graduate = models.IntegerField()
    postgraduate = models.IntegerField()
    phd = models.IntegerField()
    date_of_join = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
    others = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
        
    def get_name(self):
        return (f'{self.first_name +" " + " "+ self.middle_name +" " + " "+  self.last_name}')

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Adm_Profile'
        verbose_name_plural = 'Adm_Profiles'






GENDER = [

      ('male', 'Male'),
      ('female', 'Female')

   ]
class Admission(models.Model):
    # faculty = models.ForeignKey(to='sis.Faculty', related_name='adm_faculty', on_delete=models.CASCADE)
    # dept = models.ForeignKey(to='sis.Department', related_name='adm_department', on_delete=models.CASCADE)
    # registration_No= models.CharField(
    #        max_length = 11,
    #        blank=True,
    #        null=True,
    #        unique=True,
    #        default=create_new_ref_number()
    #   )
      
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, blank=True)
 
   
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



    def __str__(self):
        return str(self.registration_No)
        


  
    