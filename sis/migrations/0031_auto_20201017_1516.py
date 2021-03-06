# Generated by Django 3.1.2 on 2020-10-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0030_auto_20201017_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('files', models.FileField(blank=True, upload_to='rules/rule/')),
            ],
        ),
        migrations.RemoveField(
            model_name='notice',
            name='about',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='important',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='handbook',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='policy',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='rule',
        ),
        migrations.AddField(
            model_name='notice',
            name='records_forms',
            field=models.ManyToManyField(blank=True, related_name='records_file', to='sis.Notice_Files'),
        ),
        migrations.AddField(
            model_name='notice',
            name='handbook',
            field=models.ManyToManyField(blank=True, related_name='handbook_file', to='sis.Notice_Files'),
        ),
        migrations.AddField(
            model_name='notice',
            name='policy',
            field=models.ManyToManyField(blank=True, related_name='policies_file', to='sis.Notice_Files'),
        ),
        migrations.AddField(
            model_name='notice',
            name='rule',
            field=models.ManyToManyField(blank=True, related_name='rules_file', to='sis.Notice_Files'),
        ),
    ]
