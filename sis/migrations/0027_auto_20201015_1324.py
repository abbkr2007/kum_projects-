# Generated by Django 3.1.2 on 2020-10-15 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sis', '0026_auto_20201014_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=15),
        ),
        migrations.CreateModel(
            name='ProgramStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.ManyToManyField(blank=True, related_name='curent_subject_status', to='sis.Subject')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_status', to='sis.department')),
                ('faield', models.ManyToManyField(blank=True, related_name='failed_subject_status', to='sis.Subject')),
                ('nerver', models.ManyToManyField(blank=True, related_name='never_subject_status', to='sis.Subject')),
                ('passed', models.ManyToManyField(blank=True, related_name='passed_subject_status', to='sis.Subject')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pogram_status', to='sis.program')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ProgramStructure',
                'verbose_name_plural': 'ProgramStructures',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
