# Generated by Django 3.0.4 on 2020-03-23 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='signin',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='time',
            name='signout',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
