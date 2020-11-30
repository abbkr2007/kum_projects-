
from django.urls import path

from .views import *
from .import views


app_name = 'ad'

urlpatterns = [

    path('profile/',views.Ad_profile.as_view(), name='profile'),

    path('generate_card/',views.Search.as_view(), name='generate_card'),
    path('studentinfo/', views.StudentInfo.as_view(), name='studentinfo'),
  



]
