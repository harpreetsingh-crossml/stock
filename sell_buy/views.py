from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import StockTransaction, Stock, UserProfile, Transaction
from .forms import StockPurchaseForm
from .utils import fetch_stock_price


# Create your views here.

#buy stocks

@login_required

def buy_stock(request):
    if request.method == "POST":
        stock_symbol = request.POST.get("stock_symbol")
        shares = int(request.POST.get("shares"))
        
        # Perform input validation, including checking if the user can afford the purchase
        stock_price = fetch_stock_price(stock_symbol)  # You can implement this function
        total_purchase_price = stock_price * shares
        user_balance = request.user.profile.balance  # Adjust this based on your user profile structure
        
        if total_purchase_price > user_balance:
            return render(request, "apology.html", {"message": "You cannot afford this purchase."})
        
        # Deduct the purchase amount from the user's account
        request.user.profile.balance -= total_purchase_price
        request.user.profile.save()
        
        # Record the transaction in the database
        transaction = StockTransaction(
            user=request.user,
            stock_symbol=stock_symbol,
            shares=shares,
            purchase_price=total_purchase_price
        )
        transaction.save()
        
        return render(request, "confirmation.html", {"message": "Stock purchase successful!"})
    
    return render(request, "buy_stock.html")




# sell stocks

def sell_stock(request):
    if request.method == 'POST':
        stock_id = request.POST['stock_id']
        shares_to_sell = int(request.POST['shares_to_sell'])
        
        # Check if the user owns the selected stock
        user_profile = UserProfile.objects.get(user=request.user)
        stock = Stock.objects.get(pk=stock_id)
        
        if shares_to_sell <= 0 or shares_to_sell > user_profile.stock_holding(stock):
            error_message = "Invalid number of shares to sell"
        else:
            # Record the sale transaction
            transaction = Transaction(user=user_profile, stock=stock, shares_sold=shares_to_sell)
            transaction.save()
            
            # Update the user's account balance
            user_profile.balance += shares_to_sell * stock.price
            user_profile.save()
            
            success_message = "Stock sold successfully."
    
    stocks = Stock.objects.all()
    return render(request, 'sell_stock.html', {'stocks': stocks})