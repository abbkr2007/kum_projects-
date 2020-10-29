from django import forms
from django.forms import TextInput, MultiWidget, DateTimeField
from sis.models import *
from pis.models import *
from .models import*


class DateInput(forms.DateInput):
    input_type = 'date'


class Fee_Create_Form(forms.ModelForm):
    class Meta:
        model = Control_Student_Payment
        fields = '__all__'
        # exclude = ['user', 'image']

class Fee_Create_Form_Edit(forms.ModelForm):
    class Meta:
        model = Control_Student_Payment
        fields = '__all__'
        # exclude = ['user', 'image']
