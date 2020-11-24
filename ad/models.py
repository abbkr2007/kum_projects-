from django.db import models
from sis.models import Student
# Create your models here.
class Id_Card(models.Model):
    student = models.ForeignKey('sis.Student', on_delete=models.CASCADE, null=True)


class Transcript(models.Model):
    pass

class Open_Course_Registration(models.Model):
    pass

class Grade(models.Model):
    pass

class Close_Grade(models.Model):
    pass
