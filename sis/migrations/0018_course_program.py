# Generated by Django 3.1.2 on 2020-10-13 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0017_remove_program_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_course', to='sis.program'),
        ),
    ]
