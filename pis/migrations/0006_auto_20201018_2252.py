# Generated by Django 3.1.2 on 2020-10-18 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0031_auto_20201017_1516'),
        ('pis', '0005_auto_20201018_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work_load',
            name='Lecturer_course',
        ),
        migrations.AddField(
            model_name='work_load',
            name='lecturer_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='list_course_lecturer', to='sis.course'),
        ),
    ]
