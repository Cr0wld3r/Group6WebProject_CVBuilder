# Generated by Django 4.1.2 on 2022-12-18 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_job_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='short_description',
        ),
    ]
