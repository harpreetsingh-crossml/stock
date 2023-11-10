from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
from .models import StockTransaction, Stock, UserProfile, Transaction
from .forms import StockPurchaseForm
from .utils import fetch_stock_price

import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PortfolioItem
from .models import Transaction


# log in & log out views

def index(request):
     return render(request,"userside/index.html")

def user_register(request):
     if request.method == "POST":
          uname=request.POST.get('username')
          email=request.POST.get('email')
          pass1=request.POST.get('password1')
          pass2=request.POST.get('password2')
              
          if pass1!=pass2:
               return HttpResponse("your passwords are not same")
          else:
               
               my_user=User.objects.create_user(username=uname,email=email,password=pass1)
               my_user.save()
               return redirect('/user-login')

     return render (request,'userside/user_register.html')


def user_login(request):

     if request.method == "POST":
          username=request.POST.get('username')
          pass1=request.POST.get('pass')
          user=authenticate(request,username=username,password=pass1)
          if user is not None: 
               login(request,user)
               return redirect('quote')
          else:
                return HttpResponse("Username or Password is incorrect")

     return render (request,'userside/user_login.html')


def user_logout(request):
     logout(request)
     return redirect('/index')

def banner_image(request):
     return render(request, 'layout.html')


# sell buy views are here:

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



# portfolio & transaction views 

def portfolio_view(request):
    user = request.user
    portfolio_items = PortfolioItem.objects.filter(user=user)
    total_value = 0

    for item in portfolio_items:
        # Call the lookup function to get the current stock price
        response = requests.get(f'https://api.example.com/lookup?symbol={item.stock_symbol}')
        data = response.json()
        current_price = data.get('price')

        # Calculate the total value of the holding
        item.total_value = current_price * item.shares
        total_value += item.total_value

    # Retrieve user's current cash balance
    cash_balance = user.profile.cash_balance  # Replace 'profile' with the actual profile field name

    context = {
        'portfolio_items': portfolio_items,
        'total_value': total_value,
        'cash_balance': cash_balance,
    }
    return render(request, 'portfolio.html', context)


def transaction_history(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user).order_by('-date_time')
    return render(request, 'index/transaction_history.html', {'transactions': transactions})