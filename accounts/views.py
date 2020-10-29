from django.shortcuts import render, redirect, reverse
from django.views import generic


from .models import *

from .forms import *


class Ac_profile(generic.TemplateView):
    model = Account_Manager
    template_name = 'account_profile.html'

    def get_context_data(self, **kwargs):
        profile = Account_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context = {
            'profile': profile,
        }
        return context





class Add_Fees(generic.CreateView):
    model = Control_Student_Payment
    template_name = 'add_fees.html'
    form_class = Fee_Create_Form

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        return redirect("ac:fees")
           
    def get_context_data(self, **kwargs):
        self.profile = Account_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


class Fees(generic.ListView):
    model = Control_Student_Payment
    template_name = 'fees.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        self.profile = Account_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile

        return context





class Edit_Tution(generic.UpdateView):
    model = Control_Student_Payment
    form_class = Fee_Create_Form_Edit
    template_name = 'edit_fees.html'
    context_object_name = 'queryset'

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.save()
        # messages.success(self.request, 'Successfully updated your  car')
        # return redirect(reverse("student:student_edit", kwargs={
        #     'pk': form.instance.pk
        # }))
        return redirect('ac:fees')
            

    def get_context_data(self, **kwargs):
        self.profile = Account_Manager.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context

