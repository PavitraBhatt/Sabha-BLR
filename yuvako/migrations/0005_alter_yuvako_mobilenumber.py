# Generated by Django 4.2.2 on 2023-08-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuvako', '0004_alter_yuvako_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yuvako',
            name='MobileNumber',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
