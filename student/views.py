from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect



class IndexView(generic.TemplateView):

    template_name = 'index.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
           return render(request, 'teacher.html')
        else:
            return render(request, 'student.html')

    return render(request, 'index.html')


class AppView(generic.TemplateView):

    template_name = 'student.html'

class HomeView(generic.TemplateView):

    template_name = 'teacher.html'