# Generated by Django 3.1.2 on 2020-11-05 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0048_remove_faculty_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='about',
        ),
        migrations.RemoveField(
            model_name='program',
            name='faculty',
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faculty_department', to='sis.faculty'),
        ),
        migrations.AlterField(
            model_name='department',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_student', to='sis.student'),
        ),
        migrations.AlterField(
            model_name='program',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_program', to='sis.student'),
        ),
    ]
