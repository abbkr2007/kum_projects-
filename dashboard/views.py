from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from sis.views import Student_profile





def home(request):

    if request.user.is_authenticated:
        if request.user.is_teacher:
           return render(request, 'dashboard/index.html')
        else:
            return redirect('Student_profile')

    return render(request, 'dashboard/all_professors.html')


class Dash_Index(generic.TemplateView):

    template_name = 'dashboard/index.html'

class Dash_Event(generic.TemplateView):

    template_name = 'dashboard/event.html'

class Dash_all_professors(generic.TemplateView):

    template_name = 'dashboard/all_professors.html'

class Dash_add_professor_bootstrap(generic.TemplateView):

    template_name = 'dashboard/add_professor_bootstrap.html'
