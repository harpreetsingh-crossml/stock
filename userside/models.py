from django.db import models
from django.contrib.auth.models import User


# sell buy models:

#buy stocks

class StockTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_symbol = models.CharField(max_length=10)
    shares = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)


#sell stocks

class Stock(models.Model):
   symbol = models.CharField(max_length=10)
   name = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=10, decimal_places=2)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    shares_sold = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)



# portfolio & transaction

class PortfolioItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_symbol = models.CharField(max_length=10)
    shares = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shares = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=4, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol} - {self.transaction_type}"