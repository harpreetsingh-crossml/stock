from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from stock_quote.models import Stocks




# sell buy models:

# buy stocks

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=10000.0)  # Starting balance for each user

class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    shares = models.PositiveIntegerField()
    total= models.IntegerField(validators=[MaxValueValidator(10000)])
    purchase_price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


#sell stocks

class StockSell(models.Model):
    symbol = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    shares = models.CharField(max_length=100)
   

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00)

class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    shares_sold = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)



# portfolio & transaction

#portfolio
class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    shares = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2)

#transaction
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shares = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=4, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol} - {self.transaction_type}"