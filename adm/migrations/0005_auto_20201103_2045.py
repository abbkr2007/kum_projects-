# Generated by Django 3.1.2 on 2020-11-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0004_admission_registration_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='registration_No',
            field=models.CharField(blank=True, default='4526657954', max_length=10, null=True),
        ),
    ]