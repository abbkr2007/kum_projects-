
from django.urls import path

from .import views
from .views import *


app_name = 'lecturer'

urlpatterns = [

    path('profile/',views.Lecturer_profile.as_view(), name='profile'),
            
]