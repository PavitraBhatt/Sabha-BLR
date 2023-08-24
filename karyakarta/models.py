from django.db import models

# Create your models here.

class Karyakarta(models.Model):
    username = models.CharField(max_length=255)
    hashed_password = models.BinaryField()  # Store hashed password as bytes