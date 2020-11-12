# Generated by Django 3.1.2 on 2020-11-08 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0068_auto_20201109_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration_course',
            name='course_by_student',
        ),
        migrations.AddField(
            model_name='registration_course',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.student'),
        ),
    ]
