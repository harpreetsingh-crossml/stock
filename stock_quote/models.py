from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Stocks(models.Model):
    name = models.CharField(max_length=100, default= 'no')
    symbol = models.CharField(max_length=10, unique=True)
    available_shares = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    