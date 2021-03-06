# Generated by Django 3.1.2 on 2020-10-19 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0034_semester'),
        ('pis', '0009_lecturer_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sis.department')),
                ('semester', models.ManyToManyField(to='sis.Semester')),
                ('subject', models.ManyToManyField(to='sis.Subject')),
                ('sutdent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sis.student')),
            ],
            options={
                'verbose_name': 'My_Student',
                'verbose_name_plural': 'My_Students',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='My_Student',
        ),
    ]
