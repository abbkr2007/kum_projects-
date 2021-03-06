# Generated by Django 3.1.2 on 2020-10-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0040_auto_20201020_1256'),
        ('pis', '0013_auto_20201020_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_course',
            name='student',
            field=models.ManyToManyField(related_name='my_course_student', to='sis.Student'),
        ),
        migrations.AddField(
            model_name='my_course',
            name='subject',
            field=models.ManyToManyField(related_name='my_course_subject', to='sis.Subject'),
        ),
    ]
