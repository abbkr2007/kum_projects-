from django.contrib import admin

from .models import *



admin.site.register(Lecturer)
admin.site.register(Lecturer_Course)
admin.site.register(Student_Attendence)
admin.site.register(Subject_Attendence)
admin.site.register(My_Course)
admin.site.register(Work_Load)
admin.site.register(Attendance_report)
admin.site.register(Notice_Files_of_lecturer)
admin.site.register(Notice_of_lecturer)



