# Generated by Django 3.1.2 on 2020-10-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0004_auto_20201009_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
