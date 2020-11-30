from django import forms

from django.forms import TextInput, MultiWidget, DateTimeField
from sis.models import *
from pis.models import *

from .views import *
from .models import *


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









class Admission_Form(forms.ModelForm):

    class Meta:
        model = Admission
        fields = '__all__'
