# Generated by Django 4.2.2 on 2023-08-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyakarta', '0005_remove_karyakartalist_hashed_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KaryakartaList',
        ),
        migrations.RemoveField(
            model_name='karyakarta',
            name='password',
        ),
        migrations.AddField(
            model_name='karyakarta',
            name='hashed_password',
            field=models.CharField(default=models.CharField(max_length=150, unique=True), max_length=128),
        ),
        migrations.AlterField(
            model_name='karyakarta',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
