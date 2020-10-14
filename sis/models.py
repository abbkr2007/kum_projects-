from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db.models import Sum
from django.db.models import Count

STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='active')
    registration_number   = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to='students/images/')
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField(default=timezone.now)
    date_of_admission = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
    others = models.TextField(blank=True)
  
    def __str__(self):
        return self.registration_number

    def get_absolute_url(self):
        return reverse('student:sudent_detail', kwargs={
            'pk': self.pk
        })
    def get_update_url(self):
        return reverse('student:student_edit', kwargs={
            'pk': self.pk
        })

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        

Current_STATUS = [
      ('regular', 'Regular'),
      ('irregular ', 'Irregular ')
  ]
  
class CurrentStatus(models.Model):
    current_status = models.CharField(max_length=10, choices=Current_STATUS)
    # adviser
    # payment_status
    # regisration_status

    def __str__(self):
        return self.current_status

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'CurrentStatus'
        verbose_name_plural = 'CurrentStatuss'



class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    prefix = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    subject = models.ManyToManyField('Subject', related_name='subject_list', blank=True)
    program = models.ForeignKey('Program', related_name='program_course', on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.name

    def get_course_url(self):
        return reverse('student:program_detail', kwargs={
            'pk': self.pk
        })


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Program(models.Model):
    name = models.CharField(max_length=200, unique=True)
    prefix = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    year = models.IntegerField(blank=True, help_text='give a year')
    faculty = models.CharField(max_length=150, blank=True)
    department = models.ForeignKey('Department',related_name='department_pogram', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student:dept_detail', kwargs={
            'pk': self.pk
        })

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    prefix = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    about = models.CharField(max_length=150, blank=True)

    
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    
    def get_absolute_url(self):
        return reverse('student:dept_detail', kwargs={
            'pk': self.pk
        })

 


class Semester(models.Model):
    name = models.CharField(max_length=50)
    code = models.PositiveIntegerField(unique=True)
    # advior

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'



class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.PositiveIntegerField(unique=True)
    credit = models.IntegerField(blank=True)
    files = models.FileField(upload_to='course/materials/', blank=True)

    def __str__(self):
        return self.name
        

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Result_Of_Semester(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Result_Of_Semester'
        verbose_name_plural = 'Result_Of_Semesters'



class Result_Of_Dept(models.Model):
    pass


    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Result_Of_Dept'
        verbose_name_plural = 'Result_Of_Depts'



class My_Attendance(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'


class Notice(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'


