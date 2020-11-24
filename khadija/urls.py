from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from sis.admin import sis_admin_site  
from django.urls import path, include

urlpatterns = [

   
    
    path('', include('stuser.urls')),

    
    path('pustsomething/', include('dashboard.urls',)),
    
    
    path('student/', include('sis.urls', namespace='student')),
    path('lecturer/', include('pis.urls', namespace='lecturer')),
    path('hr/', include('hr.urls', namespace='hr')),
    path('account/', include('accounts.urls', namespace='ac')),
    path('adm/', include('adm.urls', namespace='adm')),

  
    # third party pakage for auth
    path('accounts/', include('allauth.urls')),





    # admin sites based on apps...
    path('admin/', admin.site.urls),
    path('sis_admin/', sis_admin_site.urls),


]






if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)




# Admin Login...............design
admin.site.site_header = "KHADIJA UNIVERSITY"
admin.site.site_title = "Uiversity Admin Portal"
admin.site.index_title = "Welcome to KHADIJA UINIVERSITY Portal"

sis_admin_site.site_header = "KHADIJA UNIVERSITY"
sis_admin_site.site_title = "SIS Admin Portal"
sis_admin_site.index_title = "Welcome to SIS Portal"