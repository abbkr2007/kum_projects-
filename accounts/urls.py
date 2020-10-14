from django.urls import path

from .import views
from .views import *

app_name = 'account'

urlpatterns = [

    path('profile/',views.Account_profile.as_view(), name='profile'),
            
]