from django.shortcuts import render

from django.views import generic
from .models import *




class Lecturer_profile(generic.TemplateView):
    model = Lecturer
    template_name = 'lecturer_profile.html'

    def get_context_data(self, **kwargs):
        profile = Lecturer.objects.all()
        context = super().get_context_data(**kwargs)
        context = {
            'profile': profile,
        }
        return context

