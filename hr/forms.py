
from django import forms
from django.forms import TextInput, MultiWidget, DateTimeField
from sis.models import *
from pis.models import *


class DateInput(forms.DateInput):
    input_type = 'date'

# class DateTimeField(forms.DateTimeField)

# Student's Forms

class Student_Profile_Edit_Form(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['user', 'image']
        
        widgets = {
            'date_of_birth':DateInput(),
            'date_of_admission': DateInput(),

        }

class Student_Create_Form(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth':DateInput(),
            'date_of_admission': DateInput(),

        }



# Lecturer's Fomrs

class Lecturer_Create_Form(forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = '__all__'
        widgets = {
            'date_of_birth':DateInput(),
            'date_of_join': DateInput(),

        }

class Lecturer_Profile_Edit_Form (forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = '__all__'
        widgets = {
            'date_of_birth':DateInput(),
            'date_of_join': DateInput(),

        }



# Workload Forms


class Workload_Update_Form(forms.ModelForm):
    class Meta:
        model = Work_Load
        fields = '__all__'

        widgets = {
            'date':DateInput(),
            'date1': DateInput(),
            'date2': DateInput(),
            'date3': DateInput(),
            'date4': DateInput(),
            'date5': DateInput(),

        }

class Workload_Create_Form(forms.ModelForm):
    class Meta:
        model = Work_Load
        fields = '__all__'

        
        widgets = {
            'date':DateInput(),
            'date1': DateInput(),
            'date2': DateInput(),
            'date3': DateInput(),
            'date4': DateInput(),
            'date5': DateInput(),

        }


  

# 'Notice' for lecturer

class Notice_Create_Form(forms.ModelForm):
    class Meta:
        model = Notice_of_lecturer
        fields = '__all__'
  

class Notice_Create_Form_Lecturer(forms.ModelForm):
    class Meta:
        model = Notice_Files_of_lecturer
        fields = '__all__'
  

class Notice_Create_Form_Edit(forms.ModelForm):
    class Meta:
        model = Notice_of_lecturer
        fields = '__all__'
  

# notice forms for student

class Notice_Create_Form_Student(forms.ModelForm):
    class Meta:
        model = Notice_Files
        fields = '__all__'
        
class Notice_Form_Student(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'

class Notice_Create_Form_Edit_Student(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'