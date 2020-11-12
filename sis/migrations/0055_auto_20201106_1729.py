# Generated by Django 3.1.2 on 2020-11-06 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0054_auto_20201106_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={},
        ),
        migrations.RemoveField(
            model_name='semester',
            name='advisor',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='code',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='course',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='department',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='program',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='session',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='student',
        ),
        migrations.AlterField(
            model_name='courses',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_courses', to='sis.program'),
        ),
        migrations.AlterModelTable(
            name='course',
            table=None,
        ),
        migrations.AlterModelTable(
            name='semester',
            table=None,
        ),
        migrations.AlterModelTable(
            name='subject',
            table=None,
        ),
    ]
