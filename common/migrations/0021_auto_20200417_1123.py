# Generated by Django 3.0.4 on 2020-04-17 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0020_auto_20200417_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('is_active', models.ImageField(max_length=200, upload_to='')),
                ('is_superuser', models.ImageField(max_length=200, upload_to='')),
                ('staff_number', models.CharField(max_length=200, null=True)),
            ],
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