
from django.urls import path

from .import views
from .views import *


app_name = 'adm'

urlpatterns = [

    path('profile/',views.Adm_profile.as_view(), name='profile'),
    path('admform/',views.Adm_View.as_view(), name='admform'),

    path('search_student/',views.Student_Search.as_view(), name='search_student'),



    
    # Student Views.......
    path('add_student/', views.Student_Create.as_view(), name='add_student'),
    path('list_of_student/', views.Student_List.as_view(), name='list_of_student'),
    path('list_of_student/<int:pk>/', views.Student_About.as_view(), name='student_about'),
    path('list_of_student/<int:pk>/update/', views.Student_edit.as_view(), name='student_edit'),

  

]
