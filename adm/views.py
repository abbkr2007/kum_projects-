from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import *
from .forms import *


class Adm_View(generic.CreateView):
    model = Admission
    template_name = 'admission_form.html'
    fields = '__all__'
    success_url = reverse_lazy('adm:admform')







