from django.db import models
from django.utils import timezone
from django.conf import settings
from sis.models import Student
# Create your models here.





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



class Ad_Profile(models.Model):
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
        verbose_name = 'Ad_Profile'
        verbose_name_plural = 'Ad_Profiles'








class Id_Card(models.Model):
    student = models.ForeignKey('sis.Student', on_delete=models.CASCADE, null=True)


class Transcript(models.Model):
    pass

class Open_Course_Registration(models.Model):
    pass

class Grade(models.Model):
    pass

class Close_Grade(models.Model):
    pass
