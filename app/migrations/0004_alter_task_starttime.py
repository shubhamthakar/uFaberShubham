# Generated by Django 3.2.9 on 2021-11-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_task_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='startTime',
            field=models.TimeField(),
        ),
    ]
