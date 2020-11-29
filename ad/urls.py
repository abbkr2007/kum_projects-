
from django.urls import path

from .views import *
from .import views


app_name = 'ad'

urlpatterns = [

    path('profile/',views.Ad_profile.as_view(), name='profile'),
    path('studentinfo/', views.StudentInfo.as_view(), name='studentinfo'),



]
