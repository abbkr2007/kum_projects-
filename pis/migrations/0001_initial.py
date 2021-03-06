# Generated by Django 3.1.2 on 2020-10-09 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sis', '0004_auto_20201009_1741'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_Load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Work_Load',
                'verbose_name_plural': 'Work_Loads',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student_Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_days', models.IntegerField()),
                ('num_of_day', models.IntegerField()),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sis.department')),
                ('semester', models.ManyToManyField(to='sis.Semester')),
                ('subject', models.ManyToManyField(to='sis.Subject')),
            ],
            options={
                'verbose_name': 'Attendence',
                'verbose_name_plural': 'Attendences',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='My_Student',
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
        migrations.CreateModel(
            name='Lecturer_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sis.department')),
                ('semester', models.ManyToManyField(to='sis.Semester')),
                ('subject', models.ManyToManyField(to='sis.Subject')),
            ],
            options={
                'verbose_name': 'Teacher_Course',
                'verbose_name_plural': 'Teacher_Courses',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('pin_number', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='lecturer/images/')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=10)),
                ('child', models.PositiveIntegerField()),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('graduate', models.IntegerField()),
                ('postgraduate', models.IntegerField()),
                ('phd', models.IntegerField()),
                ('date_of_join', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(blank=True)),
                ('others', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
