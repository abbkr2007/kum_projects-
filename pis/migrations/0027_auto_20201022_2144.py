# Generated by Django 3.1.2 on 2020-10-22 15:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0026_delete_attendance_report'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student_attendence',
            managers=[
                ('catro', django.db.models.manager.Manager()),
            ],
        ),
    ]
