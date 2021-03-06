# Generated by Django 3.1.2 on 2020-10-26 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0043_auto_20201026_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='handbook',
        ),
        migrations.AddField(
            model_name='notice',
            name='handbook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handbook_file', to='sis.notice_files'),
        ),
        migrations.RemoveField(
            model_name='notice',
            name='policy',
        ),
        migrations.AddField(
            model_name='notice',
            name='policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policies_file', to='sis.notice_files'),
        ),
        migrations.RemoveField(
            model_name='notice',
            name='records_forms',
        ),
        migrations.AddField(
            model_name='notice',
            name='records_forms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records_file', to='sis.notice_files'),
        ),
        migrations.RemoveField(
            model_name='notice',
            name='rule',
        ),
        migrations.AddField(
            model_name='notice',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rules_file', to='sis.notice_files'),
        ),
    ]
