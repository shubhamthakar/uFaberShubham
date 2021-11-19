# Generated by Django 3.2.9 on 2021-11-19 16:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='startTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='timeTaken',
            field=models.CharField(max_length=10),
        ),
    ]
