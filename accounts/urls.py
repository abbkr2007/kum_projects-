from django.urls import path

from .import views
from .views import *

app_name = 'ac'

urlpatterns = [

    path('profile/',views.Ac_profile.as_view(), name='profile'),

    path('add_tution/',views.Add_Fees.as_view(), name='add_tution'),
    path('fees/',views.Fees.as_view(), name='fees'),
    path('fees/<int:pk>/update',views.Edit_Tution.as_view(), name='edit_tution'),

            
]