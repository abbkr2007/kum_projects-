# Generated by Django 3.1.2 on 2020-11-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0035_auto_20201112_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='registration_No',
            field=models.CharField(blank=True, default='48420267877', max_length=11, null=True, unique=True),
        ),
    ]