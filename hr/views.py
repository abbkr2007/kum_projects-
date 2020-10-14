from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *




class Hr_profile(TemplateView):
    model = Hr_Manager

    template_name = 'hr_profile.html'

    def get_context_data(self, **kwargs):
        profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context = {
            'profile': profile,
        }
        return context
