# Generated by Django 3.2.9 on 2021-11-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='startTime',
            field=models.TimeField(),
        ),
    ]
