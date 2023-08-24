from django.db import models

# Create your models here.

class Yuvako(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    MobileNumber = models.IntegerField(default=00,unique=True)
    DOB = models.DateField(null=True, blank=True)
    Area = models.CharField(max_length=100)
    ReferenceName = models.CharField(max_length=100)
    Coming = models.BooleanField(default=False)