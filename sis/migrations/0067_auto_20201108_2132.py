# Generated by Django 3.1.2 on 2020-11-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0066_fine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg_course_program1',
            name='course',
        ),
        migrations.AddField(
            model_name='reg_course_program1',
            name='course',
            field=models.ManyToManyField(blank=True, to='sis.Student_Course_Name'),
        ),
    ]