# Generated by Django 3.1.2 on 2020-11-08 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0062_auto_20201108_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Course_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('credit', models.IntegerField()),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.program')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Reg_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.student_course_name')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.student')),
            ],
        ),
        migrations.RemoveField(
            model_name='semester_5th',
            name='course',
        ),
        migrations.RemoveField(
            model_name='semester_5th',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='semester_5th',
            name='program',
        ),
        migrations.RemoveField(
            model_name='semester_6th',
            name='course',
        ),
        migrations.RemoveField(
            model_name='semester_6th',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='semester_6th',
            name='program',
        ),
        migrations.RemoveField(
            model_name='semester_7th',
            name='course',
        ),
        migrations.DeleteModel(
            name='Semester_4th',
        ),
        migrations.DeleteModel(
            name='Semester_5th',
        ),
        migrations.DeleteModel(
            name='Semester_6th',
        ),
        migrations.DeleteModel(
            name='Semester_7th',
        ),
    ]