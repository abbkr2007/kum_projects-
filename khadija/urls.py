from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

   
    
    path('', include('stuser.urls')),

    
    path('pustsomething/', include('dashboard.urls',)),
    
    
    path('student/', include('sis.urls', namespace='student')),
    path('lecturer/', include('pis.urls', namespace='lecturer')),
    path('hr/', include('hr.urls', namespace='hr')),
    path('account/', include('accounts.urls', namespace='ac')),
    path('adm/', include('adm.urls', namespace='adm')),

  
    
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)