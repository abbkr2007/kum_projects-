
from django.urls import path

from .import views
from .views import *


app_name = 'adm'

urlpatterns = [

    path('profile/',views.Adm_profile.as_view(), name='profile'),
    path('admform/',views.Adm_View.as_view(), name='admform'),
  

]
