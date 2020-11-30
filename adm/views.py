from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from stuser.decorators import adm_required

from .models import *
from .forms import *
from sis.models import *
from hr.models import *




def get_booker(user):
    qs = Student.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def get_lecturer(user):
    qs = Lecturer.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None



@method_decorator([login_required, adm_required], name='dispatch')

class Student_Search(generic.View):
    
    def get(self, request, *args, **kwargs):
        self.profile = Hr_Manager.objects.all()
        queryset1 = Student.objects.all()
        query = request.GET.get('q')
        if query:
            queryset1 = queryset1.filter(Q(registration_number__exact=query)|Q(email__exact=query)).distinct()
            queryset = list(
                sorted(
                    chain(queryset1),
                    key=lambda objects: objects.pk
                ))
        context = {
            'queryset': queryset,
            'profile': self.profile,
          
        }
        return render(request, 'search_results.html', context)




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






@method_decorator([login_required, adm_required], name='dispatch')
class Student_Create(generic.CreateView):
    model = Student
    form_class = Student_Create_Form
    template_name = 'student_create.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        return redirect(reverse("adm:student_about", kwargs={
            'pk': form.instance.pk
        }))
   
    def get_context_data(self, **kwargs):
        self.profile = Adm_Profile.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context



# @method_decorator([login_required, adm_required], name='dispatch')
class Student_List(generic.ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'queryset'
    paginate_by = 1

    
    def get_context_data(self, **kwargs):
        self.profile = Adm_Profile.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, adm_required], name='dispatch')
class Student_About(generic.DetailView):
    model = Student
    template_name = 'student_about.html'
    context_object_name = 'student'


    def get_context_data(self, **kwargs):
        self.profile = Adm_Profile.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context



@method_decorator([login_required, adm_required], name='dispatch')
class Student_edit(generic.UpdateView):
    model = Student
    form_class = Student_Profile_Edit_Form
    template_name = 'edit_student.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        # messages.success(self.request, 'Successfully updated your  car')
        # return redirect(reverse("student:student_edit", kwargs={
        #     'pk': form.instance.pk
        # }))
        return redirect('adm:list_of_student')
            

    def get_context_data(self, **kwargs):
        self.profile = Adm_Profile.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        context['profile'] = self.profile
        return context
