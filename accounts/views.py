from django.shortcuts import render
from django.views.generic import TemplateView


from .models import *


class Account_profile(TemplateView):
    model = Account_Manager
    template_name = 'account_profile'

    def get_context_data(self, **kwargs):
        profile = Account_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context = {
            'profile': profile,
        }
        return context
