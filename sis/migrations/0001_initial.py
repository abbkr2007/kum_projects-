# Generated by Django 3.1.2 on 2020-10-09 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('regular', 'Regular'), ('irregular ', 'Irregular ')], max_length=10)),
            ],
            options={
                'verbose_name': 'CurrentStatus',
                'verbose_name_plural': 'CurrentStatuss',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('prefix', models.CharField(max_length=20)),
                ('code', models.PositiveIntegerField(unique=True)),
                ('duration', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='My_Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Notice',
                'verbose_name_plural': 'Notices',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Result_Of_Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Result_Of_Dept',
                'verbose_name_plural': 'Result_Of_Depts',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Result_Of_Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Result_Of_Semester',
                'verbose_name_plural': 'Result_Of_Semesters',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Semester',
                'verbose_name_plural': 'Semesters',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('registration_number', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='students/images/')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('date_of_admission', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(blank=True)),
                ('others', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
