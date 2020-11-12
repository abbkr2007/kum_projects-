from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from stuser.models import CustomUser
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from stuser.decorators import sis_required
from .models import *
from .forms import *

def get_booker(user):
    qs = Student.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


@method_decorator([login_required, sis_required], name='dispatch')
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



@method_decorator([login_required, sis_required], name='dispatch')
class Course_metarial(generic.View):
    def get(self, *args, **kwargs):
        profile = Student.objects.filter(user=self.request.user)
        department = Department.objects.filter(student__user=self.request.user)
        program = Program.objects.filter(student__user=self.request.user)
        course = Course.objects.filter(student__user=self.request.user)
        like = Course.objects.filter(student__user=self.request.user).annotate(total_credit=Sum('subject__credit'))

        context = {
            'dept':department,
            'program':program,
            'course':course,
            'queryset':like,
            'profile': profile,
        }
        return render(self.request, 'metarial.html', context)



@method_decorator([login_required, sis_required], name='dispatch')
class Student_Course_Names(generic.ListView):
    model = Choice_Course
    template_name = 'student_course_name.html'
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        profile = Student.objects.filter(user=self.request.user)
        total_credit = Choice_Course.objects.filter(student__user=self.request.user).aggregate(
            total_credit=Sum('course__credit')
        )['total_credit'] or 0

        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['total'] = total_credit
        return context

        

@method_decorator([login_required, sis_required], name='dispatch')
class Program_structure(generic.View):

    def get(self, *args, **kwargs):
        profile = Student.objects.all()
        profilee = get_object_or_404(Student, user=self.request.user)
        program_structure = Course.objects.filter(student=profilee)



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
    paginate_by = 2

    def get_context_data(self, **kwargs):
        profile = Student.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context
  

class Dept_detail(generic.DetailView, MultipleObjectMixin):  
    model = Department
    template_name = 'programs.html'
    context_object_name = 'queryset'
    paginate_by = 2

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

    def get_context_data(self, **kwargs):
        self.profile = Student.objects.all()
        object_list = Semester.objects.filter(program=self.object)
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['program'] = Program.objects.all()
        context['profile'] = self.profile
        return context


class Course_detail(generic.DetailView):
    model = Semester
    template_name = 'course_detail.html'
    queryset = Semester.objects.annotate(
        total_credit=Sum('course__credit')
    )
    context_object_name = 'queryset'
    
    
    def get_context_data(self, **kwargs):
        self.profile = Student.objects.all()
      
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile 
        return context


@method_decorator([login_required, sis_required], name='dispatch')
class Notice_files(generic.TemplateView):
    model = Student
    template_name = 'notice_student.html'

    def get_context_data(self, **kwargs):
        profile = Student.objects.filter(user=self.request.user)
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

@method_decorator([login_required, sis_required], name='dispatch')
class ContactView(generic.FormView):
    # model = Category
    form_class = ContactForm
    success_url = reverse_lazy('student:contact') # we can have a specific page here..
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        profile = Student.objects.filter(user=self.request.user)
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







class Semester_View(generic.ListView):
    model = Program
    template_name = 'test/test.html'
    context_object_name = 'queryset'




@method_decorator([login_required, sis_required], name='dispatch')
class Course_Registration(generic.CreateView):
    model = Choice_Course  
    template_name = 'test/reg.html'
    form_class = RegForm
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        profile = Student.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context


    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        return redirect('student:reg')

           






class Message_View(generic.View):

    def get(self, *args, **kwargs):

        profile = get_object_or_404(Student, user=self.request.user)
        data = Student_Message.objects.filter(student=profile)
        
        context = {
            'data':data,
           
        }
        return render(self.request, 'message.html', context)



def message_view(request):
    if request.method != "POST":
        # messages.error(request, "Invalid Method")
        print("it's not POST")
        return redirect('student:message')
    else:
        message = request.POST.get('message')
        data = get_object_or_404(Student, user=request.user)
        try:
            leave_report = Student_Message(student=data, message=message, message_status=0)
            leave_report.save()
            print(leave_report)
            print("hi from else")
            # messages.success(request, "Applied for Leave.")
            return redirect('student:message')
        except:
            print("it's doesn't work")
            # messages.error(request, "Failed to Apply Leave")
            return redirect('student:message')


