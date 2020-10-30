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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='active')
    registration_number   = models.CharField(max_length=100, unique=True)
    dept = models.ForeignKey('Department', related_name='student_department', on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to='students/images/')
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField(default=timezone.now)
    date_of_admission = models.DateField(default=timezone.now)
    join = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
    others = models.TextField(blank=True)

  
  
    def __str__(self):
        return self.registration_number

    def get_name(self):
        return (f'{self.first_name +" " + " "+ self.middle_name +" " + " "+  self.last_name}')


    def get_absolute_url(self):
        return reverse('hr:student_about', kwargs={
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


class SessionYearModel(models.Model):
    session_start_year = models.DateField()
    session_end_year = models.DateField()

class Semester_Session(models.Model):
    name = models.CharField(max_length=100)
    session_start= models.DateField()
    session_end = models.DateField()


class CurrentStatus(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True)
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

        
Subject_Status = [
      ('available', 'Available'),
      ('unavailable', 'Unavailable')
  ]


class Subject(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    code = models.PositiveIntegerField(unique=True)
    credit = models.IntegerField(blank=True)
    files = models.FileField(upload_to='course/materials/', blank=True)
    status = models.CharField(max_length=20, choices=Subject_Status, blank=True)

    def __str__(self):
        return self.name
        

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'





class Course(models.Model):
    # tracking student course 
    # also tracking course result by the student 

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, unique=True)
    prefix = models.CharField(max_length=20)
    code = models.CharField(max_length=20)

    subject = models.ManyToManyField('Subject', related_name='subject_list', blank=True)

    # result of student by the courses
    faield = models.ManyToManyField(Subject,related_name='failed_subject_status', blank=True)
    passed = models.ManyToManyField(Subject,related_name='passed_subject_status', blank=True)
    nerver = models.ManyToManyField(Subject,related_name='never_subject_status', blank=True)
    current = models.ManyToManyField(Subject,related_name='curent_subject_status', blank=True)
    

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
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True)
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
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True)
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
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='semester_dept', blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, related_name='semester_program', blank=True, null=True)
    # course = models.ForeignKey(Course, related_name='semester_course', on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ManyToManyField(Course, related_name='semester_course', blank=True)
    student = models.ManyToManyField(Student, related_name='semester_student', blank=True)
    session = models.ForeignKey(Semester_Session, on_delete=models.SET_NULL, related_name='semester_program', blank=True, null=True)
    code = models.CharField(max_length=40)
    advisor = models.ForeignKey(to='pis.Lecturer', on_delete=models.SET_NULL, related_name='semester_advisor', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'



 




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


class Notice_Files(models.Model):

    name = models.CharField(max_length=100, blank=True)
    files = models.FileField(upload_to='rules/rule/', blank=True)

    def __str__(self):
        return self.name
   


class Notice(models.Model):
    name = models.CharField(max_length=100, blank=True)
    handbook = models.ForeignKey(Notice_Files, related_name='handbook_file', on_delete=models.CASCADE, null=True, blank=True)
    rule = models.ForeignKey(Notice_Files, related_name='rules_file', on_delete=models.CASCADE, null=True, blank=True)
    records_forms = models.ForeignKey(Notice_Files, related_name='records_file', on_delete=models.CASCADE, null=True, blank=True)
    policy = models.ForeignKey(Notice_Files, related_name='policies_file', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
        

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'









# class ProgramStructure(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
#     department = models.ForeignKey('Department',related_name='department_status', on_delete=models.CASCADE, blank=True, null=True)
#     program = models.ForeignKey('Program',related_name='pogram_status', on_delete=models.CASCADE, blank=True, null=True)
#     course = models.ForeignKey('Course',related_name='course_status', on_delete=models.CASCADE, blank=True, null=True)

#     faield = models.ManyToManyField(Subject,related_name='failed_subject_status', blank=True)
#     passed = models.ManyToManyField(Subject,related_name='passed_subject_status', blank=True)
#     nerver = models.ManyToManyField(Subject,related_name='never_subject_status', blank=True)
#     current = models.ManyToManyField(Subject,related_name='curent_subject_status', blank=True)
    
#     def __str__(self):
#         return str(self.user)

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'ProgramStructure'
#         verbose_name_plural = 'ProgramStructures'


































