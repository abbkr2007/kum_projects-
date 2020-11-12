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
    registration_number = models.CharField(max_length=100, unique=True)
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

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/user.jpg"

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


        
Current_STATUS = [
      ('regular', 'Regular'),
      ('irregular ', 'Irregular ')
  ]



class CurrentStatus(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True)
    current_status = models.CharField(max_length=10, choices=Current_STATUS)
    faculty = models.ForeignKey('Faculty', related_name='student_curent_faculty', on_delete=models.SET_NULL, blank=True, null=True)
    dept = models.ForeignKey('Department', related_name='student_curent_department', on_delete=models.SET_NULL, blank=True, null=True)
    program = models.ForeignKey('Program', related_name='student_curent_program', on_delete=models.SET_NULL, blank=True, null=True)
    semester = models.ForeignKey('Semester', related_name='student_courent_semester', on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return self.current_status

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'CurrentStatus'
        verbose_name_plural = 'CurrentStatuss'

        



class SessionYearModel(models.Model):
    session_start_year = models.DateField()
    session_end_year = models.DateField()
  
class Semester_Session(models.Model):
    name = models.CharField(max_length=100)
    session_start= models.DateField()
    session_end = models.DateField()




class Faculty(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Faculty'
        verbose_name_plural = 'Facultys'
 


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, related_name='faculty_department', on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, related_name='department_student', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, unique=True)
    prefix = models.CharField(max_length=20)
    code = models.CharField(max_length=20)

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
 

class Program(models.Model):
    student = models.ForeignKey(Student, related_name='student_program', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey('Department', related_name='department_program', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    prefix = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    year = models.IntegerField(blank=True, help_text='give a year')
    
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



class Courses(models.Model):  # Subject 
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, related_name='program_courses', on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length=10)
    credit = models.IntegerField()

    def __str__(self):
        return (f'{self.name}, {self.program}, {self.code}')




class Semester(models.Model): # Course
    name = models.CharField(max_length=50)
    program = models.ForeignKey(Program, related_name='semester_program', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ManyToManyField(Courses, related_name='semester_course')

    def __str__(self):
        return (f'{self.name},{self.program}')


    def get_course_url(self):
        return reverse('student:program_detail', kwargs={
            'pk': self.pk
        })





class Course_Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    currentstatus = models.ForeignKey(CurrentStatus, related_name='student_course_reg', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.student)













































































Subject_Status = [
      ('available', 'Available'),
      ('unavailable', 'Unavailable')
  ]

class Subject(models.Model): # this now works as Courses.....Subject = Course
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    code = models.PositiveIntegerField(unique=True)
    credit = models.IntegerField(blank=True)
    files = models.FileField(upload_to='course/materials/', blank=True)
    status = models.CharField(max_length=20, choices=Subject_Status, blank=True)

    def __str__(self):
        return self.name




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




class Student_Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True )
    message = models.TextField()
    message_status = models.IntegerField(default=0)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.student)


class Semester_1st(models.Model):
    name = models.CharField(max_length=100) # 1st Semeseter
    dept = models.ForeignKey(Department, related_name='department_1st_semester', on_delete=models.CASCADE, blank=True, null=True)
    program = models.ForeignKey(Program, related_name='program_1st_semester', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ManyToManyField(Courses) 
    
    def __str__(self):
        return (f'{self.name}, {self.dept}, {self.program}')

class Semester_2nd(models.Model):
    name = models.CharField(max_length=100) 
    dept = models.ForeignKey(Department, related_name='department_2nd_semester', on_delete=models.CASCADE, blank=True, null=True)
    program = models.ForeignKey(Program, related_name='program_2nd_semester', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ManyToManyField(Courses) 
    
    def __str__(self):
       return (f'{self.name}, {self.dept}, {self.program}')

class Semester_3rd(models.Model):
    name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, related_name='department_3rd_semester', on_delete=models.CASCADE, blank=True, null=True)
    program = models.ForeignKey(Program, related_name='program_3rd_semester', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ManyToManyField(Courses) 
    
    def __str__(self):
        return (f'{self.name}, {self.dept}, {self.program}')




























# you will be talking thoses course during your semesters......

class Student_Course_Name(models.Model):                                              # 1 Program courses
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credit = models.IntegerField()

    def __str__  (self):
        return (f'{self.faculty},{self.dept},{self.program},{self.name}')


class Choice_Course(models.Model): #list of courses show for student.....just show him ....      Program1
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ManyToManyField(Student_Course_Name, blank=True)

    def __str__(self):
        return str(self.student)



# resgistrations Froms for course........                                    program1 registration
class Registration_Course(models.Model):
    # course_by_student = models.ForeignKey(Choice_Course, on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ManyToManyField(Student_Course_Name, blank=True)

    def __str__(self):
        return str(self.course)











































class Fine(models.Model):
    q = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    z = models.CharField ('Fine', max_length=100)

    def __str__(self):
        return self.z




















