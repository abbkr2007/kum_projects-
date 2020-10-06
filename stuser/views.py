from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm



class Signup(generic.TemplateView):
    template_name = 'stuser/signup.html'

# class RegisterView(generic.CreateView):
#     template_name = 'stuser/register.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('IndexView')


class StudentRegisterView(generic.CreateView):
    template_name = 'stuser/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Index')



class TeacherRegisterView(generic.CreateView):
    template_name = 'stuser/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')