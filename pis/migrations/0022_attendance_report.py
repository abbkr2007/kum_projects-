# Generated by Django 3.1.2 on 2020-10-22 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0021_auto_20201022_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('present', models.PositiveIntegerField()),
                ('absent', models.IntegerField()),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_attendance', to='pis.student_attendence')),
            ],
        ),
    ]
