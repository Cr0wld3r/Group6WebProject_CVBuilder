# Generated by Django 4.1.2 on 2022-12-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_builder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='school',
            new_name='previous_work_title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='about_you',
        ),
        migrations.AddField(
            model_name='profile',
            name='gpa',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='previous_work_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='year_graduate',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.TextField(max_length=1000),
        ),
    ]