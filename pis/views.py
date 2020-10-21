from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic
from .models import *
from .forms import *


def get_booker(user):
    qs = Lecturer.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


class Lecturer_profile(generic.TemplateView):
    model = Lecturer
    template_name = 'lecturer_profile.html'

    def get_context_data(self, **kwargs):
        profile = Lecturer.objects.all()
        context = super().get_context_data(**kwargs)
        context = {
            'profile': profile,
        }
        return context



class Lecturer_edit(generic.UpdateView):
    model = Lecturer
    form_class = Lecturer_Profile_Form
    template_name = 'lecturer_edit.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        # messages.success(self.request, 'Successfully updated your  car')
        return redirect(reverse("lecturer:lecturer_edit", kwargs={
            'pk': form.instance.pk
        }))

    def get_context_data(self, **kwargs):
        self.profile = Lecturer.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        context['profile'] = self.profile
        return context





class Course_by_teacher(generic.ListView):
    model = My_Course
    template_name = 'my_course.html'
    context_object_name = 'queryset'
    
    def get_context_data(self, **kwargs):
        profile = Lecturer.objects.all()
        semester_course = My_Course.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['test'] = semester_course
        return context


class My_Course_detail(generic.DetailView):
    model = My_Course
    template_name = 'my_course_detail.html'
    # queryset = Course.objects.annotate(
    #     total_credit=Sum('subject__credit')
    # )
    context_object_name = 'queryset'
    
    
    def get_context_data(self, **kwargs):
        self.profile = Lecturer.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context



class Workload(generic.TemplateView):
    model = Work_Load
    template_name = 'workload.html'

    def get_context_data(self, *args, **kwargs):
        profile = Lecturer.objects.all()
        workload = Work_Load.objects.all()
        context = super().get_context_data(**kwargs)
        context = {
            'profile':profile,
            'workload':workload
        }
        return context
        
class ContactView(generic.FormView):
    # model = Category
    form_class = ContactForm
    success_url = reverse_lazy('lecturer:l_contact') # we can have a specific page here..
    template_name = 'l_contact.html'

    def get_context_data(self, **kwargs):
        profile = Lecturer.objects.all()
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