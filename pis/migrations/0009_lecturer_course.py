# Generated by Django 3.1.2 on 2020-10-19 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0034_semester'),
        ('pis', '0008_auto_20201019_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecturer_dept', to='sis.department')),
                ('semester', models.ManyToManyField(blank=True, related_name='lecturer_semester', to='sis.Semester')),
                ('subject', models.ManyToManyField(related_name='lecturer_subject', to='sis.Subject')),
            ],
            options={
                'verbose_name': 'Lecturer_Course',
                'verbose_name_plural': 'Lecturer_Courses',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
