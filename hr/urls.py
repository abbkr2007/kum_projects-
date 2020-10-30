from django.urls import path

from .import views


app_name = 'hr'

urlpatterns = [

    path('profile/',views.Hr_profile.as_view(), name='profile'),


    # Search Views......
    path('search_student/',views.Student_Search.as_view(), name='search_student'),
    path('search_lecturer/',views.Lecturer_Search.as_view(), name='search_lecturer'),
    # path('search_student/',views.Student_Search.as_view(), name='search'),

    

    # Lecturer Views......
    path('add_lecturer/', views.Lecturer_Create.as_view(), name='add_lecturer'),
    path('list_of_lecturer/', views.Lecturer_List.as_view(), name='list_of_lecturer'),
    path('list_of_lecturer/<int:pk>/', views.Lecturer_About.as_view(), name='lecturer_about'),
    path('list_of_lecturer/<int:pk>/update/', views.Lecturer_edit.as_view(), name='lecturer_edit'),


    #Attendanece
    path('select_sub_teacher/', views.Select_subject_lecturer.as_view(), name='select_sub_teacher'),
    path('select_subject/',views.Attendance_create_subject.as_view(), name='select_subject'),
    

    # Course Managerment Views......]
    path('lecturer_courses_create/', views.Lecturer_Course_Create.as_view(), name='lecturer_courses_create'),
    path('lecturer_courses/', views.Course_For_Lecturer.as_view(), name='lecturer_courses'),
    
  

    # path('attendance/take_attendance/',views.Attendance_create.as_view(), name='attendence_create'),


    # Student Views.......
    path('add_student/', views.Student_Create.as_view(), name='add_student'),
    path('list_of_student/', views.Student_List.as_view(), name='list_of_student'),
    path('list_of_student/<int:pk>/', views.Student_About.as_view(), name='student_about'),
    path('list_of_student/<int:pk>/update/', views.Student_edit.as_view(), name='student_edit'),


    # WorkLoad views......
    path('add_workload/', views.Add_Workload.as_view(), name='add_workload'),
    path('workload_list/', views.WorkLoad_View.as_view(), name='workload_list'),
    path('workload_list/<int:pk>/update', views.WorkLoad_Update.as_view(), name='workload_update'),




    # Notice System for Lecturer
    path('add_notice_lecturer/', views.Add_Notice_For_Lecturer.as_view(), name='add_notice_lecturer'),
    path('add_notice/', views.Notice_Create.as_view(), name='add_notice'),
    path('notice_list/', views.Notice_List.as_view(), name='notice_list',),
    path('edit_notice_lecturer/<int:pk>/update/', views.Notice_edit_Lecturer.as_view(), name='edit_notice_lecturer'),
    path('delete_notice_lecturer/<int:pk>/delete/', views.Notice_Delete.as_view(), name='delete_notice_lecturer'),


    # Notice System for Student
    path('add_notice_student/', views.Add_Notice_For_Student.as_view(), name='add_notice_student'),
    path('add_notice_for_student/', views.Notice_Create_Student.as_view(), name='add_notice_for_student'),
    path('notice_list_student/', views.Notice_List_Student.as_view(), name='notice_list_student'),
    path('edit_notice_student/<int:pk>/update/', views.Notice_edit_Student.as_view(), name='edit_notice_student'),
    path('delete_notice_student/<int:pk>/delete/', views.Notice_Delete_Student.as_view(), name='delete_notice_student'),

    
  
            
]