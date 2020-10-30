
from django.urls import path

from .import views
from .views import *


app_name = 'lecturer'

urlpatterns = [

    path('profile/',views.Lecturer_profile.as_view(), name='profile'),

     
    path('attend/',views.Attendance_List_View.as_view(), name='attend'),

    path('attend/<int:pk>/update',views.Attendance_Update_View.as_view(), name='student_attendance_edit'),




    path('my_course/',views.Course_by_teacher.as_view(), name='my_course'),
    path('my_course/<int:pk>/',views.My_Course_detail.as_view(), name='my_course_detail'),



    

    path('attendance/',views.Student_attendance_subject.as_view(), name='attendance'),
    path('attendance/take_attendance/',views.Attendance_create.as_view(), name='attendence_create'),
    path('attendance/<int:pk>/',views.Attendence_detail.as_view(), name='student_attendance'),






  
    # path('attendance/<int:pk>/update/', views.Attendance_edit.as_view(), name='student_attendance_edit'),





















    path('workload/',views.Workload.as_view(), name='workload'),

    path('guide_line/', views.Notice_files.as_view(), name='guide_line'),
    path('l_contact/', views.ContactView.as_view(), name='l_contact'),

    
    
            
]