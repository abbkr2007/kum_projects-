from django.urls import path

from .import views
from .views import *


app_name = 'hr'

urlpatterns = [

    path('profile/',views.Hr_profile.as_view(), name='profile'),
            
]