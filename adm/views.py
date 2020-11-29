from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from stuser.decorators import adm_required

from .models import *
from .forms import *







@method_decorator([login_required, adm_required], name='dispatch')
class Adm_profile(generic.TemplateView):
    model = Adm_Profile
    template_name = 'adm_profile.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        profile = Adm_Profile.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context

  

@method_decorator([login_required, adm_required], name='dispatch')
class Adm_View(generic.CreateView):
    model = Admission
    template_name = 'admission_form.html'
    fields = '__all__'
    success_url = reverse_lazy('adm:admform')







