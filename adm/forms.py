from django import forms

from .views import *
from .models import *

class Admission_Form(forms.ModelForm):

    class Meta:
        model = Admission
        fields = '__all__'
