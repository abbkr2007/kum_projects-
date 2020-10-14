from django.db import models

# Create your models here.



def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
           return render(request, 'teacher.html')
        else:
            return render(request, 'student.html')

    return render(request, 'index.html')
