# Generated by Django 3.1.2 on 2020-11-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0029_auto_20201108_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='registration_No',
            field=models.CharField(blank=True, default='76651704193', max_length=11, null=True, unique=True),
        ),
    ]