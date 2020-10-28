from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('stu/', include('student.urls', namespace='app')),
    
    path('', include('dashboard.urls',)),
    
    path('account/', include('accounts.urls', namespace='ac')),
    path('hr/', include('hr.urls', namespace='hr')),
    path('lecturer/', include('pis.urls', namespace='lecturer')),
    path('student/', include('sis.urls', namespace='student')),

    path('stuser/', include('stuser.urls')),
    
    path('accounts/', include('allauth.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)