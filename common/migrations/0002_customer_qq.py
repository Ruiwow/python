# Generated by Django 2.2.9 on 2020-01-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='qq',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
