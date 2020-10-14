from django.urls import path
from .import views
from .views import *




urlpatterns = [

    path('',views.Dash_Index.as_view(), name='index'),
    path('check/', home, name='check'),
    path('event/',views.Dash_Event.as_view(), name='event'),
    path('all_professors/',views.Dash_all_professors.as_view(), name='all_professors'),
    path('add_professor_bootstrap/',views.Dash_add_professor_bootstrap.as_view(), name='add_professor_bootstrap'),

            
]