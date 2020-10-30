from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound


def home(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            return redirect('student:profile')
        elif request.user.is_teacher:
            return redirect('lecturer:profile')
        elif request.user.is_hr:
            return redirect('hr:profile')
        elif request.user.is_account:
            return redirect('account:profile')
        elif request.user.is_superuser:
            return HttpResponse('<a href="http://127.0.0.1:8000/admin/">Yes, Please</a>')
        else:
            return redirect('account_login')

            
    return redirect('account_login')
    # link of University Main page
    # return render(request, 'account_login')
