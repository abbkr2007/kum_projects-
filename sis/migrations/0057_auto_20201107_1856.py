# Generated by Django 3.1.2 on 2020-11-07 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0056_auto_20201106_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='student',
        ),
        migrations.RemoveField(
            model_name='program',
            name='student',
        ),
    ]
