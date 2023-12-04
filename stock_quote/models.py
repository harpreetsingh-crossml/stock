from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Stocks(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    