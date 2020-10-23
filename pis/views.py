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
        profile = Lecturer.objects.filter(user=self.request.user)
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
        self.profile = Lecturer.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        context['profile'] = self.profile
        return context





class Course_by_teacher(generic.ListView):
    model = My_Course
    template_name = 'my_course.html'
    context_object_name = 'queryset'
    
    def get_context_data(self, **kwargs):
        profile = Lecturer.objects.filter(user=self.request.user)
        semester_course = My_Course.objects.filter(lecturer__user=self.request.user)
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
        self.profile = Lecturer.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context








class Attendance_List_View(generic.ListView):
    model = Student_Attendence
    template_name = 'attend_list.html'
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        profile = Lecturer.objects.all()
        semester_course = Subject_Attendence.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['test'] = semester_course
        return context


class Attendance_Update_View(generic.UpdateView):
    model = Student_Attendence
    template_name = 'attend_update.html'
    form_class = Attendance_Form
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        profile = Lecturer.objects.all()
        semester_course = Subject_Attendence.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['test'] = semester_course
        return context

    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        return redirect(reverse("lecturer:student_attendance_edit", kwargs={
            'pk': form.instance.pk
        }))




class Student_attendance_subject(generic.ListView):
    model = Subject_Attendence
    template_name = 'attendence.html'
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        profile = Lecturer.objects.all()
        semester_course = Subject_Attendence.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['test'] = semester_course
        return context



class Attendence_detail(generic.DetailView):
    model = Subject_Attendence
    template_name = 'attendence_details.html'
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        profile = Lecturer.objects.all()
        semester_course = Student_Attendence.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['test'] = semester_course
        return context



class Attendance_create_subject(generic.CreateView):
    model = Subject_Attendence
    form_class = Student_Attendance_Form
    template_name = 'attendance_edit_subject.html'

    def get_context_data(self, *args, **kwargs):
        profile = Lecturer.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context

    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        return redirect('lecturer:attendance')


class Attendance_create(generic.CreateView):
    model = Student_Attendence
    form_class = Student_Form
    template_name = 'attendance_edit.html'
    
    def get_context_data(self, *args, **kwargs):
        profile = Lecturer.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context


    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        return redirect(reverse("lecturer:student_attendance", kwargs={
            'pk': form.instance.pk
        }))






# class Update(generic.UpdateView):
#     model = Student_Attendance
#     form_class = Student_Attendance_Form
#     template_name = 'edit.html'
#     context_object_name = 'queryset'

#     def form_valid(self, form):
#         form.instance.CustomUser = get_booker(self.request.user)
#         form.save()
#         # messages.success(self.request, 'Successfully updated your  car')
#         return redirect(reverse("lecturer:edit", kwargs={
#             'pk': form.instance.pk
#         }))

#     def get_context_data(self, **kwargs):
#         self.profile = Lecturer.objects.all()
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Update'
#         context['profile'] = self.profile
#         return context








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







class Notice_files(generic.TemplateView):
    model = Lecturer
    template_name = 'notice_lecturer.html'

    def get_context_data(self, **kwargs):
        profile = Lecturer.objects.filter()
        notice = Notice_of_lecturer.objects.all()
        context = super().get_context_data(**kwargs)
        context = {

            'profile': profile,
            'notice': notice,
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