# Generated by Django 3.1.2 on 2020-11-28 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0071_registration_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration_course',
            name='student',
        ),
    ]
