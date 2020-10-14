from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_account = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
