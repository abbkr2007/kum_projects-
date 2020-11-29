from django.db import models
from django.utils import timezone
from django.conf import settings
from pis.models import *
from sis.models import *

# 6 HR - STAFF- Superuser

# 2. Staff email creation
# 3. department responsibility   ;;;;; SuperUser for PIS 
# 4. primary duty
# 5. secondary duty if any



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


class Hr_Manager(models.Model):
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
        verbose_name = 'Hr_Manager'
        verbose_name_plural = 'Hr_Managers'


# 1. Staff registration - ID, login detail


# class Control_Staff(models.Model):

#     def __str__(self):
#         pass

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Control_Staff'
#         verbose_name_plural = 'Control_Staffs'



class Control_Lecturer(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, blank=True, null=True)
    # lecturer = models.ManyToManyField(Lecturer, related_name='leacturer_files', blank=True)
    files = models.FileField(upload_to='hr/files/')
    notice = models.TextField()
    text = models.CharField(max_length=150)


    def __str__(self):
        return self.lecturer

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Control_Lecturer'
        verbose_name_plural = 'Control_Lecturers'



class Control_Student(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    # student = models.ManyToManyField(Lecturer, related_name='student_files', blank=True)
    files = models.FileField(upload_to='sis/files/')
    notice = models.TextField()
    text = models.CharField(max_length=150)


    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Control_Student'
        verbose_name_plural = 'Control_Students'