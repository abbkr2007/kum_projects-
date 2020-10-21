
from django.urls import path

from .import views
from .views import *


app_name = 'lecturer'

urlpatterns = [

    path('profile/',views.Lecturer_profile.as_view(), name='profile'),
    path('profile/<int:pk>/update/', views.Lecturer_edit.as_view(), name='lecturer_edit'),



    path('my_course/',views.Course_by_teacher.as_view(), name='my_course'),
    
    path('my_course/<int:pk>/',views.My_Course_detail.as_view(), name='my_course_detail'),
















    path('workload/',views.Workload.as_view(), name='workload'),
    path('l_contact/', views.ContactView.as_view(), name='l_contact'),

    
    
            
]