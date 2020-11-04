
from django.urls import path

from .import views
from .views import *


app_name = 'adm'

urlpatterns = [

    path('admform/',views.Adm_View.as_view(), name='admform'),
  

]
