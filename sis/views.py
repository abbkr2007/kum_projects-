from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from stuser.models import CustomUser
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import get_object_or_404
from django.db.models import Sum

from .models import *
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
        profile = Student.objects.filter(user=self.request.user)
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


class Course_metarial(generic.View):

    def get(self, *args, **kwargs):
        profile = Student.objects.all()
        department = Department.objects.filter(user=self.request.user)
        program = Program.objects.filter(user=self.request.user)
        course = Course.objects.filter(user=self.request.user)
        like = Course.objects.filter(user=self.request.user).annotate(total_credit=Sum('subject__credit'))

        context = {
            'dept':department,
            'program':program,
            'course':course,
            'queryset':like,
            'profile': profile,
        }
        return render(self.request, 'metarial.html', context)



class Program_structure(generic.View):

    def get(self, *args, **kwargs):
        profile = Student.objects.all()
        profilee = get_object_or_404(Student, user=self.request.user)
        program_structure = Course.objects.filter(student=profilee)
        # program_structure = Course.objects.filter(student__user=self.request.user)


        credit = Course.objects.filter(student__user=self.request.user).annotate(total_no=Sum('subject__credit'))

        total_credit = program_structure.aggregate(
            total_credit=Sum('subject__credit')
        )['total_credit'] or 0

        context = {
            'test':program_structure,
            'credit':credit,
            'profile':profile,
            'total_credit' : total_credit
        }
        return render(self.request, 'program_structure.html', context)



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



class Notice_files(generic.TemplateView):
    model = Student
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        profile = Student.objects.filter()
        notice = Notice.objects.all()
        context = super().get_context_data(**kwargs)
        context = {

            'profile': profile,
            'notice': notice,
        }
        return context

class Event(generic.TemplateView):
    model = Student
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        profile = Student.objects.filter()
        context = super().get_context_data(**kwargs)
        context = {

            'profile': profile,
    
        }
        return context

class ContactView(generic.FormView):
    # model = Category
    form_class = ContactForm
    success_url = reverse_lazy('student:contact') # we can have a specific page here..
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        profile = Student.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        from_email = form.cleaned_data['email']
        message = form.cleaned_data['message']  
        try:
            send_mail(name, message, from_email, ['admin@example.com'])
            # messages.warning(self.request, "Your email sent successfuly")
        except BadHeaderError:
            # messages.warning(self.request, "Your email didn't successfuly")
            return HttpResponse('Invalid header found.')
        return super(ContactView, self).form_valid(form)




