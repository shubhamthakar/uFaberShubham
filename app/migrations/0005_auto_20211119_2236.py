# Generated by Django 3.2.9 on 2021-11-19 17:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_task_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='startTime',
            field=models.TimeField(default=datetime.datetime(2021, 11, 19, 22, 36, 31, 69146)),
        ),
        migrations.AlterField(
            model_name='task',
            name='timeTaken',
            field=models.TimeField(max_length=10),
        ),
    ]