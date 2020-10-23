from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


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
        
    def get_update_url(self):
        return reverse('lecturer:lecturer_edit', kwargs={
            'pk': self.pk
        })



class Lecturer_Course(models.Model):
    department = models.ForeignKey(to='sis.Department', related_name='lecturer_dept', on_delete=models.SET_NULL, blank=True, null=True)
    semester = models.ManyToManyField(to='sis.Semester', related_name='lecturer_semester', blank=True)
    subject = models.ManyToManyField(to='sis.Subject', related_name='lecturer_subject')

    def __str__(self):
        return str(self.department)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Lecturer_Course'
        verbose_name_plural = 'Lecturer_Courses'




class My_Course(models.Model):
    name = models.CharField(max_length=20)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, related_name='my_course_lecturer', blank=True, null=True)
    department = models.ForeignKey(to='sis.Department', on_delete=models.SET_NULL, blank=True, null=True)
    semester = models.ForeignKey(to='sis.Semester', on_delete=models.SET_NULL, related_name='my_course_semester', blank=True, null=True)
    subject = models.ManyToManyField(to='sis.Subject',  related_name='my_course_subject')
    course = models.ForeignKey(to='sis.Course', on_delete=models.SET_NULL, related_name='my_course_course', blank=True, null=True)
    student = models.ManyToManyField(to='sis.Student', related_name='my_course_student')

    def __str__(self):
        return str(self.department)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'My_Course'
        verbose_name_plural = 'My_Courses'

    def get_absolute_url(self):
        return reverse('lecturer:my_course_detail', kwargs={
            'pk': self.pk
        })







class Subject_Attendence(models.Model):
    # Track Subject
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey(to='sis.Department', on_delete=models.SET_NULL, blank=True, null=True)
    semester =models.ForeignKey(to='sis.Semester', on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.ForeignKey(to='sis.Subject', on_delete=models.SET_NULL, blank=True, null=True)
    hour = models.CharField(max_length=50, blank=True, null=True)
 
    
    def __str__(self):
        return str(self.subject)
    
    
    def get_absolute_url(self):
        return reverse('lecturer:student_attendance', kwargs={
            'pk': self.pk
        })


    def get_update_url(self):
        return reverse('lecturer:subject_attendance_edit', kwargs={
            'pk': self.pk
        })


class Student_Attendence(models.Model):
    # TrackStudent
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.ForeignKey(Subject_Attendence, related_name='subject_attendance', on_delete=models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(to='sis.Student', on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    present_days = models.PositiveIntegerField(blank=True, null=True)
    absent_days = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.student)
    
    
    def get_absolute_url(self):
        return reverse('lecturer:student_attendence_detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('lecturer:student_attendance_edit', kwargs={
            'pk': self.pk
        })

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Student_Attendence'
        verbose_name_plural = 'Student_Attendences'
    



class Attendance_report(models.Model):
    subject = models.ForeignKey(Subject_Attendence, related_name='subject_attendance_reprot', on_delete=models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(Student_Attendence, related_name='student_attendance_report', on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    attend = models.BooleanField(default=False)

    def __str__(self):
        return str(self.student)
    
    def get_absolute_url(self):
        return reverse('lecturer:attendence_report', kwargs={
            'pk': self.pk
        })
    





Work_status = [
      ('part time', 'Part Time'),
      ('full time', 'Full Time')
  ]

Education_level = [

      ('a', 'A'),
      ('b', 'B'),
      ('c', 'C'),
      ('d', 'D'),
  ]

class Work_Load(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, blank=True, null=True)
    work_status = models.CharField(max_length=10, choices=Work_status,blank=True, null=True)
    education_level = models.CharField(max_length=10, choices=Education_level, blank=True)

    lecturer_dept = models.ForeignKey(to='sis.Department', on_delete=models.SET_NULL, related_name='dept_of_lecturer', blank=True, null=True)
    lecturer_program = models.ForeignKey(to='sis.Program',on_delete=models.SET_NULL,related_name='program_of_lecturer',blank=True, null=True)
    lecturer_course = models.ForeignKey(to='sis.Course', on_delete=models.SET_NULL, related_name='list_course_lecturer', blank=True, null=True)

    subject1 = models.ForeignKey(to='sis.Subject',on_delete=models.SET_NULL,related_name='list_subject_lecturer1',blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    subject6 = models.ForeignKey(to='sis.Subject',on_delete=models.SET_NULL,related_name='list_subject_lecturer6',blank=True, null=True)
    date1 = models.DateTimeField(blank=True, null=True)
    subject2 = models.ForeignKey(to='sis.Subject',on_delete=models.SET_NULL,related_name='list_subject_lecturer2',blank=True, null=True)
    date2 = models.DateTimeField(blank=True, null=True)
    subject3 = models.ForeignKey(to='sis.Subject',on_delete=models.SET_NULL,related_name='list_subject_lecturer3',blank=True, null=True)
    date3 = models.DateTimeField(blank=True, null=True)
    subject4 = models.ForeignKey(to='sis.Subject',on_delete=models.SET_NULL,related_name='list_subject_lecturer4',blank=True, null=True)
    date4 = models.DateTimeField(blank=True, null=True)
    subject5 = models.ForeignKey(to='sis.Subject',on_delete=models.SET_NULL,related_name='list_subject_lecturer5',blank=True, null=True)
    date5 = models.DateTimeField(blank=True, null=True)

    # Lecturer_course = models.ManyToManyField(Course, related_name='list_course_lecturer', blank=True)
    
    # Lecturer_subject = models.ManyToManyField(Subject, related_name='list_subject_lecturer', blank=True)
   

    

    def __str__(self):
        return str(self.lecturer)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Work_Load'
        verbose_name_plural = 'Work_Loads'




class Notice_Files_of_lecturer(models.Model):

    name = models.CharField(max_length=100, blank=True)
    files = models.FileField(upload_to='rules/rule/', blank=True)

    def __str__(self):
        return self.name
   

class Notice_of_lecturer(models.Model):
    name = models.CharField(max_length=100, blank=True)
    handbook = models.ManyToManyField(Notice_Files_of_lecturer, related_name='handbook_file', blank=True)
    rule = models.ManyToManyField(Notice_Files_of_lecturer, related_name='rules_file', blank=True)
    records_forms = models.ManyToManyField(Notice_Files_of_lecturer, related_name='records_file', blank=True)
    policy = models.ManyToManyField(Notice_Files_of_lecturer, related_name='policies_file', blank=True)
    
    def __str__(self):
        return self.name
        

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Notice_of_lecturer'
        verbose_name_plural = 'Notice_of_lecturers'

