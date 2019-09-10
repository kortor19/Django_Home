from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    phoneno = models.CharField(max_length=11)
    email = models.EmailField(blank = False, null = False)
    role = models.CharField(max_length=50)
    address = models.TextField()


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=11)
    address = models.TextField()
