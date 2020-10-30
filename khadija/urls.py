from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

   
    
    path('', include('stuser.urls')),

    
    path('pustsomething/', include('dashboard.urls',)),
    
    path('account/', include('accounts.urls', namespace='ac')),
    path('hr/', include('hr.urls', namespace='hr')),
    path('lecturer/', include('pis.urls', namespace='lecturer')),
    path('student/', include('sis.urls', namespace='student')),

  
    
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)