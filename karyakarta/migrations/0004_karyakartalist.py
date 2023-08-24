# Generated by Django 4.2.2 on 2023-08-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyakarta', '0003_rename_password_karyakarta_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KaryakartaList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('hashed_password', models.CharField(max_length=128)),
            ],
        ),
    ]