# Generated by Django 3.0.4 on 2020-04-17 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0027_auto_20200417_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phonenumber',
        ),
        migrations.AlterField(
            model_name='clocktime',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='common.Staff'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='common.Staff'),
        ),
    ]
