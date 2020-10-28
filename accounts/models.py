from django.db import models
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


class Account_Manager(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='active')
    pin_number   = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='acc/images/')
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
        verbose_name = 'Account_Manager'
        verbose_name_plural = 'Account_Managers'


class Tution_Fee(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    total_tution = models.PositiveIntegerField()

    def __str__(self):
        return str(self.dept)



class Control_Student_Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    tuton_fee = models.ForeignKey(Tution_Fee, on_delete=models.SET_NULL, blank=True, null=True)
    paid = models.PositiveIntegerField(blank=True, null=True)
    invoice = models.CharField(max_length=100, null=True, blank=True)
    # date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.student)

    def payble(self):
        bar = self.tuton_fee.total_tution - self.paid
        return bar



class Course_Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    course_fee = models.PositiveIntegerField()

    def __str__(self):
         return str(self.student)








# 1. Staff registration - ID, login detail


# class Control_Staff(models.Model):

#     def __str__(self):
#         pass

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Control_Staff'
#         verbose_name_plural = 'Control_Staffs'



# class Control_Lecturer_Salary(models.Model):
#     lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, blank=True, null=True)
#     # lecturer = models.ManyToManyField(Lecturer, related_name='leacturer_files', blank=True)
#     files = models.FileField(upload_to='acc/files/')
#     notice = models.TextField()
#     text = models.CharField(max_length=150)


#     def __str__(self):
#         return self.lecturer

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Control_Lecturer'
#         verbose_name_plural = 'Control_Lecturers'





