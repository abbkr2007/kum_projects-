# Generated by Django 3.1.2 on 2020-10-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0022_attendance_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance_report',
            name='absent',
        ),
        migrations.RemoveField(
            model_name='attendance_report',
            name='present',
        ),
        migrations.RemoveField(
            model_name='student_attendence',
            name='absent',
        ),
        migrations.RemoveField(
            model_name='student_attendence',
            name='present',
        ),
        migrations.AddField(
            model_name='attendance_report',
            name='attend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student_attendence',
            name='attend',
            field=models.BooleanField(default=False),
        ),
    ]