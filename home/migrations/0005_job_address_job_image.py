# Generated by Django 4.1.2 on 2022-12-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_job_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
