from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def sis_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='account_login'):

    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.

    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_student,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def pis_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='account_login'):

    '''
    Decorator for views that checks that the 
    logged in user is a teacher,
    redirects to the log-in page if necessary

    '''
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_teacher,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def hr_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='account_login'):

    '''
    Decorator for views that checks that the 
    logged in user is a teacher,
    redirects to the log-in page if necessary

    '''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_hr,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def ac_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='account_login'):

    '''
    Decorator for views that checks that the 
    logged in user is a teacher,
    redirects to the log-in page if necessary

    '''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_account,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def adm_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='account_login'):

    '''
    Decorator for views that checks that the 
    logged in user is a teacher,
    redirects to the log-in page if necessary

    '''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_adm,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def ad_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='account_singup'):

    '''
    Decorator for views that checks that the 
    logged in user is a teacher,
    redirects to the log-in page if necessary

    '''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_ad,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
