from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from stuser.decorators import ad_required

from sis.models import Student
from .models import *
# from .forms import *





@method_decorator([login_required, ad_required], name='dispatch')
class Ad_profile(generic.TemplateView):
    model = Ad_Profile
    template_name = 'ad_profile.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        profile = Ad_Profile.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context 


@method_decorator([login_required, ad_required], name='dispatch')
class StudentInfo(generic.ListView):
    model = Student
    template_name = 'studentinfo.html'
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        info = Student.objects.all()
        context = super().get_context_data(**kwargs)
        context['info'] = info
        return context











