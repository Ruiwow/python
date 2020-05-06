# Generated by Django 3.0.4 on 2020-05-05 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0048_auto_20200505_1113'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.AlterField(
            model_name='clocktime',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Staff'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='common.Staff'),
        ),
    ]
