# Generated by Django 4.1.2 on 2022-12-18 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_builder', '0004_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]