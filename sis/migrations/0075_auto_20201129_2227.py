# Generated by Django 3.1.2 on 2020-11-29 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0074_auto_20201129_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sis_department', to='sis.department'),
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sis_faculty', to='sis.faculty'),
        ),
        migrations.AddField(
            model_name='student',
            name='registration_No',
            field=models.CharField(blank=True, default='84050539388', max_length=11, null=True, unique=True),
        ),
    ]
