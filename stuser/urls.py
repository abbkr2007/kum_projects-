from django.urls import path 

from .import views
from sis.views import Student_profile
from pis.views import Lecturer_profile
from .hub import home
app_name = 'stuser'

urlpatterns = [

  
    path('', home, name='home'),




    # path('register/',views.RegisterView.as_view(), name='register'),
    # path('login/', views.LoginView.as_view(), name='login'),
    
    path('signup/',views.Signup.as_view(), name='signup'),

    path('student/register/',views.StudentRegisterView.as_view(), name='student_register'),

    path('teacher/register/',views.TeacherRegisterView.as_view(), name='teacher_register'),


]


