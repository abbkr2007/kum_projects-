from django.contrib import admin
from .models import *

from django.contrib.admin import AdminSite

class SIS_Admin_Site(AdminSite):

    admin.site.site_header = "KHADIJA UNIVERSITY"
    admin.site.site_title = "Uiversity Admin Portal"
    admin.site.index_title = "Welcome to KHADIJA UINIVERSITY Portal"

sis_admin_site = SIS_Admin_Site(name='sis_admin')



# Model register....
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'registration_number', 'status', 'gender', 'phone', 'email')
    list_filter = ('status',)
    search_fields = ('registration_number',)

sis_admin_site.register(Student, StudentAdmin)

# sis_admin_site.register(CurrentStatus)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'code', 'prefix')
  
sis_admin_site.register(Department, DepartmentAdmin)

# sis_admin_site.register(Semester_Session)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'code', 'prefix')
    search_fields = ('name',)

sis_admin_site.register(Program, ProgramAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'program', 'code', 'credit')
    search_fields = ('name',)

sis_admin_site.register(Courses, CoursesAdmin)



sis_admin_site.register(Semester)
sis_admin_site.register(Faculty)
sis_admin_site.register(Notice)
sis_admin_site.register(Subject)
sis_admin_site.register(Course)
sis_admin_site.register(Notice_Files)



sis_admin_site.register(Registration_Course)



sis_admin_site.register(Student_Course_Name)


sis_admin_site.register(Choice_Course)



# admin.site.register(Semester_2nd)
# admin.site.register(Semester_3rd)
