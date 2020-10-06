from django.urls import path 

from .import views
from .views import home, IndexView, AppView, HomeView

app_name = 'app'

urlpatterns = [
    
    path('',views.IndexView.as_view(), name='index'),

    path('check/',home, name='home'),

    path('students/',views.AppView.as_view(), name='students'),

    path('teachers/',views.HomeView.as_view(), name='teachers'),


]