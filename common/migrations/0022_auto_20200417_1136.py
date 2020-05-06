# Generated by Django 3.0.4 on 2020-04-17 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_auto_20200417_1123'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='photo',
        ),
        migrations.AddField(
            model_name='articles',
            name='is_active',
            field=models.ImageField(max_length=200, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='articles',
            name='is_superuser',
            field=models.ImageField(max_length=200, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='articles',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='staff_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='username',
            field=models.CharField(max_length=200, null=True),
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