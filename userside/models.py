from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from stock_quote.models import Stocks
from django.utils import timezone


# sell buy models:

# buy stocks

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=10000.0)  # Starting balance for each user

class Stock(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(default=0.0, max_digits=1000, decimal_places=2)
    shares = models.IntegerField(default=0)
    total= models.IntegerField(default=0, validators=[MaxValueValidator(10000)])
    purchase_price = models.DecimalField(default=0.0, max_digits=10000, decimal_places=2,)
    date_time = models.DateTimeField(default=timezone.now)

 

#sell stocks

class StockSell(models.Model):
    symbol = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    shares = models.ImageField(max_length=100)
   


# portfolio & transaction

#portfolio

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)



#transaction

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(default='no', max_length=255)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    shares = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=255, choices=[('BUY', 'Buy'), ('SELL', 'Sell')], null=False)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.transaction_type} - {self.symbol} - {self.date_time}"


