from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from stuser.models import CustomUser
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Sum
from .forms import *

def get_booker(user):
    qs = Student.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

class Student_profile(generic.TemplateView):
    model = Student
    template_name = 'student_profile.html'

    def get_context_data(self, **kwargs):
        profile = Student.objects.all()
        context = super().get_context_data(**kwargs)
        context = {

            'profile': profile,
        }
        return context


class Student_edit(generic.UpdateView):
    model = Student
    form_class = Student_Profile_Form
    template_name = 'edit_student.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        # messages.success(self.request, 'Successfully updated your  car')
        return redirect(reverse("student:student_edit", kwargs={
            'pk': form.instance.pk
        }))

    def get_context_data(self, **kwargs):
        self.profile = Student.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        context['profile'] = self.profile
        return context


class Department_courses(generic.ListView):
    model = Department
    template_name = 'deparments.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        profile = Student.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context
  

class Dept_detail(generic.DetailView, MultipleObjectMixin):
    model = Department
    template_name = 'programs.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        self.profile = Student.objects.all()
        object_list = Program.objects.filter(department=self.object)
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['department'] = Department.objects.all()
        context['profile'] = self.profile
        return context


class Program_detail(generic.DetailView, MultipleObjectMixin):
    model = Program
    template_name = 'courses.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        self.profile = Student.objects.all()
        object_list = Course.objects.filter(program=self.object)
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['program'] = Program.objects.all()
        context['profile'] = self.profile
        
        return context


class Course_detail(generic.DetailView):
    model = Course
    template_name = 'course_detail.html'
    queryset = Course.objects.annotate(
        total_credit=Sum('subject__credit')
    )
    context_object_name = 'queryset'
    
    
    def get_context_data(self, **kwargs):
        self.profile = Student.objects.all()
      
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile

 
        return context

