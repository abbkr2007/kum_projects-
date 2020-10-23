
from django import forms
# from tinymce.widgets import TinyMCE
# from tinymce import TinyMCE
from .models import Lecturer, Student_Attendence, Subject_Attendence



class DateInput(forms.DateInput):
    input_type = 'date'

class Lecturer_Profile_Form(forms.ModelForm):

    class Meta:
        model = Lecturer
        exclude = ['user', 'image']
        widgets = {
            'date_of_birth':DateInput(),
            'date_of_join': DateInput(),

        }




class Student_Attendance_Form(forms.ModelForm):

    class Meta:
        model = Subject_Attendence
        exclude = ['lecturer']
        widgets = {
            'date':DateInput(),
            # 'date_of_admission': DateInput(),

        }

class Attendance_Form(forms.ModelForm):

    class Meta:
        model = Student_Attendence
        exclude = ['lecturer']
        widgets = {
            'date':DateInput(),
            # 'date_of_admission': DateInput(),

        }

class Student_Form(forms.ModelForm):

    class Meta:
        model = Student_Attendence
        exclude = ['lecturer']
        widgets = {
            'date':DateInput(),
            # 'date_of_admission': DateInput(),

        }





class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)