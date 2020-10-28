from django.shortcuts import render
from django.views import generic


from .models import *


class Ac_profile(generic.TemplateView):
    model = Account_Manager
    template_name = 'account_profile.html'

    def get_context_data(self, **kwargs):
        profile = Account_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context = {
            'profile': profile,
        }
        return context


class Fees(generic.ListView):
    model = Control_Student_Payment
    template_name = 'fees.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        self.profile = Account_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile

        return context
