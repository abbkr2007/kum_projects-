# Generated by Django 3.1.2 on 2020-11-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0032_auto_20201108_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='registration_No',
            field=models.CharField(blank=True, default='14323873171', max_length=11, null=True, unique=True),
        ),
    ]
