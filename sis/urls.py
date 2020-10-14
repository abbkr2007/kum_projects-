
from django.urls import path

from .import views
from .views import *


app_name = 'student'

urlpatterns = [

    path('profile/',views.Student_profile.as_view(), name='profile'),
    path('profile/<int:pk>/update/', views.Student_edit.as_view(), name='student_edit'),

    path('department/',views.Department_courses.as_view(), name='departments'),
    path('department/program/<int:pk>/', views.Dept_detail.as_view(), name='dept_detail'),

    path('department/program/course/<int:pk>/', views.Program_detail.as_view(), name='program_detail'),

    path('department/program/course/details/<int:pk>/', views.Course_detail.as_view(), name='course_detail'),
            
]