# Generated by Django 3.1.2 on 2020-10-13 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0015_auto_20201013_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='program',
        ),
        migrations.AddField(
            model_name='program',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_pogram', to='sis.department'),
        ),
        migrations.AlterField(
            model_name='program',
            name='course',
            field=models.ManyToManyField(blank=True, to='sis.Course'),
        ),
    ]
