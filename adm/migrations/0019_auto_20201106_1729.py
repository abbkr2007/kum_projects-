# Generated by Django 3.1.2 on 2020-11-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0018_auto_20201106_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='registration_No',
            field=models.CharField(blank=True, default='91777819303', max_length=11, null=True, unique=True),
        ),
    ]
