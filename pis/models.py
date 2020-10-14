from django.db import models
from django.conf import settings
from django.utils import timezone
from sis.models import Student, Department, Semester, Subject


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

class Lecturer(models.Model):
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

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Lecturer_Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    semester = models.ManyToManyField(Semester)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return str(self.department)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Lecturer_Course'
        verbose_name_plural = 'Lecturer_Courses'


class Student_Attendence(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    semester =models.ForeignKey(Semester, on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    num_of_days = models.IntegerField()
    num_of_day = models.IntegerField()

    def __str__(self):
        return str(self.num_of_day)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Student_Attendence'
        verbose_name_plural = 'Student_Attendences'


class My_Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    semester = models.ManyToManyField(Semester)
    subject = models.ManyToManyField(Subject)
    sutdent = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.sutdent)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'My_Student'
        verbose_name_plural = 'My_Students'


class Work_Load(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Work_Load'
        verbose_name_plural = 'Work_Loads'