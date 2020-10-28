from django.urls import path

from .import views
from .views import *

app_name = 'ac'

urlpatterns = [

    path('profile/',views.Ac_profile.as_view(), name='profile'),

    path('fees/',views.Fees.as_view(), name='fees'),

            
]