# Generated by Django 4.2.2 on 2023-08-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuvako', '0002_yuvako_coming'),
    ]

    operations = [
        migrations.AddField(
            model_name='yuvako',
            name='MobileNumber',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='yuvako',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]
