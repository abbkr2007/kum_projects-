# Generated by Django 3.1.2 on 2020-11-28 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sis', '0072_remove_registration_course_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Close_Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Open_Course_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Id_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.student')),
            ],
        ),
        migrations.CreateModel(
            name='Ad_Profile',
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
                'verbose_name': 'Ad_Profile',
                'verbose_name_plural': 'Ad_Profiles',
                'db_table': '',
                'managed': True,
            },
        ),
    ]