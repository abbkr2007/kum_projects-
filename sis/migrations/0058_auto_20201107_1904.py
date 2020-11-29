# Generated by Django 3.1.2 on 2020-11-07 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0057_auto_20201107_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_student', to='sis.student'),
        ),
        migrations.AddField(
            model_name='program',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_program', to='sis.student'),
        ),
    ]