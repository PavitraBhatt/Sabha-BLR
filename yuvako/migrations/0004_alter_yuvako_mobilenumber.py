# Generated by Django 4.2.2 on 2023-08-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuvako', '0003_yuvako_mobilenumber_alter_yuvako_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yuvako',
            name='MobileNumber',
            field=models.IntegerField(default=0, null=True, unique=True),
        ),
    ]
