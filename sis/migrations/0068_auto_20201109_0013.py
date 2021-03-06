# Generated by Django 3.1.2 on 2020-11-08 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0067_auto_20201108_2132'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reg_Course_Program1',
            new_name='Choice_Course',
        ),
        migrations.CreateModel(
            name='Registration_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(blank=True, to='sis.Student_Course_Name')),
                ('course_by_student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.choice_course')),
            ],
        ),
    ]
