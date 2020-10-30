from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


from .forms import CustomUserCreationForm, CustomUserChangeForm



class Signup(generic.TemplateView):
    template_name = 'stuser/signup.html'

# class RegisterView(generic.CreateView):
#     template_name = 'stuser/register.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('IndexView')



class LoginView(generic.FormView):
    """login view"""

    form_class = forms.LoginForm
    success_url = reverse_lazy('stuser:home')
    template_name = 'stuser/login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data

        user = authenticate(username=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('stuser:login'))




class StudentRegisterView(generic.CreateView):
    template_name = 'stuser/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Index')



class TeacherRegisterView(generic.CreateView):
    template_name = 'stuser/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')