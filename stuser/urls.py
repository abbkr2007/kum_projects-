from django.urls import path 

from .import views

app_name = 'stuser'

urlpatterns = [

    # path('register/',views.RegisterView.as_view(), name='register'),

    path('',views.Signup.as_view(), name = 'signup'),

    path('student/register/',views.StudentRegisterView.as_view(), name='student_register'),

    path('teacher/register/',views.TeacherRegisterView.as_view(), name='teacher_register'),


]


