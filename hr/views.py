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
from django.db.models import Sum, Count, Q
from itertools import chain

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from stuser.decorators import hr_required


from .models import *
from .forms import *
from sis.models import *
from pis.models import *


# def get_booker(user):
#     qs = Student.objects.filter(user=user)
#     if qs.exists():
#         return qs[0]
#     return None


# def get_lecturer(user):
#     qs = Lecturer.objects.filter(user=user)
#     if qs.exists():
#         return qs[0]
#     return None





@method_decorator([login_required, hr_required], name='dispatch')
class Lecturer_Search(generic.View):
    
    def get(self, request, *args, **kwargs):
        self.profile = Hr_Manager.objects.all()
        queryset2 = Lecturer.objects.all()  
        query = request.GET.get('q')
        if query:
            queryset2 = queryset2.filter(Q(pin_number__exact=query)|Q(email__exact=query)).distinct()
            queryset = list(
                sorted(
                    chain(queryset2),
                    key=lambda objects: objects.pk
                ))
        context = {
            'queryset': queryset,
            'profile': self.profile,
          
        }
        return render(request, 'search_results_lecturer.html', context)



# class Student_Search(generic.View):
    
#     def get(self, request, *args, **kwargs):
#         self.profile = Hr_Manager.objects.all()
#         queryset1 = Student.objects.all()
#         queryset2 = Lecturer.objects.all()
#         # queryset3 = FeaturedPost.objects.all()
#         # queryset4 = Recipe.objects.all()
#         query = request.GET.get('q')
#         if query:
#             queryset1 = queryset1.filter(Q(registration_number__exact=query)|Q(email__exact=query)).distinct()
#             # queryset2 = queryset2.filter(Q(pin_number__exact=query)|Q(email__exact=query)).distinct()
#             # queryset3 = queryset3.filter(Q(title__icontains=query)|Q(overview__icontains=query)).distinct()
#             # queryset4 = queryset4.filter(Q(title__icontains=query)|Q(overview__icontains=query)).distinct()
#             queryset = list(
#                 sorted(
#                     chain(queryset1, queryset2),
#                     key=lambda objects: objects.pk
#                 ))
#         context = {
#             'queryset': queryset,
#             'profile': self.profile,
          
#         }
#         return render(request, 'search_results.html', context)




@method_decorator([login_required, hr_required], name='dispatch')
class Hr_profile(generic.TemplateView):
    model = Hr_Manager
    template_name = 'hr_profile.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context




# Control Lecturer's 
# Control Lecturer's 


@method_decorator([login_required, hr_required], name='dispatch')
class Lecturer_Create(generic.CreateView):
    model = Lecturer
    form_class = Lecturer_Create_Form
    template_name = 'lecturer_create.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        
        form.instance.CustomUser = get_lecturer(self.request.user)
        form.save()
        return redirect(reverse("hr:lecturer_about", kwargs={
            'pk': form.instance.pk
        }))
   
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class Lecturer_List(generic.ListView):
    model = Lecturer
    template_name = 'lecturer_list.html'
    context_object_name = 'queryset'

    
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context
    


@method_decorator([login_required, hr_required], name='dispatch')
class Lecturer_About(generic.DetailView):
    model = Hr_Manager
    template_name = 'lecturer_about.html'
    context_object_name = 'lecturer'

    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class Lecturer_edit(generic.UpdateView):
    model = Lecturer
    form_class = Lecturer_Profile_Edit_Form
    template_name = 'edit_lecturer.html'
    context_object_name = 'queryset'
    paginate_by = 1


    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        # messages.success(self.request, 'Successfully updated your  car')
        # return redirect(reverse("student:student_edit", kwargs={
        #     'pk': form.instance.pk
        # }))
        return redirect('hr:list_of_lecturer')
            

    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        context['profile'] = self.profile
        return context



## control Attendance

class Select_subject_lecturer(generic.ListView):
    model = Subject_Attendence
    template_name = 'subject_lecturer.html'
    context_object_name = 'queryset'


    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
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
        return redirect('hr:select_sub_teacher')






# Student Control Plan
# Student Control Plan

# @method_decorator([login_required, hr_required], name='dispatch')
# class Student_Create(generic.CreateView):
#     model = Student
#     form_class = Student_Create_Form
#     template_name = 'student_create.html'
#     context_object_name = 'queryset'

#     def form_valid(self, form):
#         form.instance.CustomUser = get_booker(self.request.user)
#         form.save()
#         return redirect(reverse("hr:student_about", kwargs={
#             'pk': form.instance.pk
#         }))
   
#     def get_context_data(self, **kwargs):
#         self.profile = Hr_Manager.objects.all()
#         context = super().get_context_data(**kwargs)
#         context['profile'] = self.profile
#         return context

  

# @method_decorator([login_required, hr_required], name='dispatch')
# class Student_List(generic.ListView):
#     model = Student
#     template_name = 'student_list.html'
#     context_object_name = 'queryset'
#     paginate_by = 1

    
#     def get_context_data(self, **kwargs):
#         self.profile = Hr_Manager.objects.all()
#         context = super().get_context_data(**kwargs)
#         context['profile'] = self.profile
#         return context


# @method_decorator([login_required, hr_required], name='dispatch')
# class Student_About(generic.DetailView):
#     model = Student
#     template_name = 'student_about.html'
#     context_object_name = 'student'


#     def get_context_data(self, **kwargs):
#         self.profile = Hr_Manager.objects.all()
#         context = super().get_context_data(**kwargs)
#         context['profile'] = self.profile
#         return context


# @method_decorator([login_required, hr_required], name='dispatch')
# class Student_edit(generic.UpdateView):
#     model = Student
#     form_class = Student_Profile_Edit_Form
#     template_name = 'edit_student.html'
#     context_object_name = 'queryset'

#     def form_valid(self, form):
#         form.instance.CustomUser = get_booker(self.request.user)
#         form.save()
#         # messages.success(self.request, 'Successfully updated your  car')
#         # return redirect(reverse("student:student_edit", kwargs={
#         #     'pk': form.instance.pk
#         # }))
#         return redirect('hr:list_of_student')
            

#     def get_context_data(self, **kwargs):
#         self.profile = Hr_Manager.objects.all()
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Update'
#         context['profile'] = self.profile
#         return context



# Course Management


@method_decorator([login_required, hr_required], name='dispatch')
class Course_For_Lecturer(generic.ListView):
    model = My_Course
    template_name = 'course_for_lecturer.html'
    context_object_name = 'queryset'

    
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class Lecturer_Course_Create(generic.CreateView):
    model = My_Course
    form_class = Lecturer_Course_Create_Form
    template_name = 'lecturer_course_create.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        return redirect('hr:lecturer_courses')
   
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context

  
# @method_decorator([login_required, hr_required], name='dispatch')
# class Student_edit(generic.UpdateView):
#     model = Student
#     form_class = Student_Profile_Edit_Form
#     template_name = 'edit_student.html'
#     context_object_name = 'queryset'

#     def form_valid(self, form):
#         form.instance.CustomUser = get_booker(self.request.user)
#         form.save()
#         # messages.success(self.request, 'Successfully updated your  car')
#         # return redirect(reverse("student:student_edit", kwargs={
#         #     'pk': form.instance.pk
#         # }))
#         return redirect('hr:list_of_student')
            

#     def get_context_data(self, **kwargs):
#         self.profile = Hr_Manager.objects.all()
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Update'
#         context['profile'] = self.profile
#         return context








# Workload System

@method_decorator([login_required, hr_required], name='dispatch')
class Add_Workload(generic.CreateView):
    model = Work_Load
    template_name = 'workload_create.html'
    form_class = Workload_Create_Form

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        return redirect("hr:workload_list")
           
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class WorkLoad_View(generic.ListView):
    model = Work_Load
    template_name = 'workload_list.html'
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class WorkLoad_Update(generic.UpdateView):
    model = Work_Load
    form_class = Workload_Update_Form
    template_name = 'workload_update.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = get_booker(self.request.user)
        form.save()
        # messages.success(self.request, 'Successfully updated your  car')
        # return redirect(reverse("student:student_edit", kwargs={
        #     'pk': form.instance.pk
        # }))
        return redirect('hr:workload_list')

    def get_context_data(self, *args, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context








## Notice Systems

@method_decorator([login_required, hr_required], name='dispatch')
class Add_Notice_For_Lecturer(generic.CreateView):
    model = Notice_Files_of_lecturer
    template_name = 'add_notice_lecturer.html'
    form_class = Notice_Create_Form_Lecturer

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        return redirect("hr:notice_list")
           
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


       

@method_decorator([login_required, hr_required], name='dispatch')
class Notice_List(generic.ListView):
    model = Notice_of_lecturer
    template_name = 'notice.html'
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class Notice_Create(generic.CreateView):
    model = Notice_of_lecturer
    template_name = 'notice_create.html'
    form_class = Notice_Create_Form

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        return redirect("hr:notice_list")
           
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context




@method_decorator([login_required, hr_required], name='dispatch')
class Notice_edit_Lecturer(generic.UpdateView):
    model = Notice_of_lecturer
    form_class = Notice_Create_Form_Edit
    template_name = 'edit_notice_lecturer.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        # messages.success(self.request, 'Successfully updated your  car')
        # return redirect(reverse("student:student_edit", kwargs={
        #     'pk': form.instance.pk
        # }))
        return redirect('hr:notice_list')
            

    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class Notice_Delete(generic.DeleteView):
    model = Notice_of_lecturer
    success_url = reverse_lazy('hr:notice_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)







## Notice System For Student



@method_decorator([login_required, hr_required], name='dispatch')
class Add_Notice_For_Student(generic.CreateView):
    model = Notice_Files
    template_name = 'add_notice_student.html'
    form_class = Notice_Create_Form_Student

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        return redirect("hr:notice_list_student")
           
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class Notice_List_Student(generic.ListView):
    model = Notice
    template_name = 'notice_list_student.html'
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context



@method_decorator([login_required, hr_required], name='dispatch')
class Notice_Create_Student(generic.CreateView):
    model = Notice
    template_name = 'notice_create_student.html'
    form_class = Notice_Form_Student

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        return redirect("hr:notice_list_student")
           
    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class Notice_edit_Student(generic.UpdateView):
    model = Notice
    form_class = Notice_Create_Form_Edit_Student
    template_name = 'edit_notice_student.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        # messages.success(self.request, 'Successfully updated your  car')
        # return redirect(reverse("student:student_edit", kwargs={
        #     'pk': form.instance.pk
        # }))
        return redirect('hr:notice_list_student')
            

    def get_context_data(self, **kwargs):
        self.profile = Hr_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


@method_decorator([login_required, hr_required], name='dispatch')
class Notice_Delete_Student(generic.DeleteView):
    model = Notice
    success_url = reverse_lazy('hr:notice_list_student')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


