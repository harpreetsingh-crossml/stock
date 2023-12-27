from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .models import Stock, StockSell, UserProfile, Transaction
from .models import Portfolio
from .forms import BuyStockForm, SellStockForm
from .utils import get_stock_price
import requests

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Transaction
from stock_quote.models import Stocks
from .models import Transaction

# log in & log out views

def index(request):
     return render(request,"userside/index.html")

def home(request):
     return render(request,"userside/home.html")



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
               return redirect('stock_quote:quote')
          else:
               messages.error(request, 'Invalid username or password. Please try again.')

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
    if request.method == 'POST':
            form = BuyStockForm(request.POST)
            if form.is_valid():
                symbol = form.cleaned_data['symbol']
                shares = form.cleaned_data['shares']
                price = request.POST.get ('price')

                stock_data = Stocks.objects.get(symbol=symbol)


                if price is not None:
                    total = shares * price
                else:
                    total = 0 


                user = UserProfile.objects.get(user=request.user)
                account_balance = user.account_balance
                if account_balance >= total:
                    # Deduct the purchase amount from the user's account
                    user.account_balance -= total
                    user.save()
                    
                    # Record the transaction ""
                    transaction = Transaction.objects.create(
                        user=user,
                        symbol=symbol,
                        shares=shares,
                        price=price,
                        
                    )
                    transaction.save()


                    return render(request, 'userside/confirmation.html', {'transaction': transaction})
                else:
                    return render(request, 'userside/apology.html', {'message': 'Insufficient funds.'})
    else:
            form = BuyStockForm()

    return render(request, 'userside/buy_stocks.html', {'form': form})


# sell stocks

@login_required

def sell_stock(request):
    
    if request.method == 'POST':
        form = SellStockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            shares = form.cleaned_data['shares']
            price = request.POST.get ('price')
            stock_data = Stocks.objects.get(symbol=symbol)
            account_balance = 1000
        
           # user = request.user
            #user_account = UserProfile.objects.get(user=user)
            
           # Check if the user can afford the purchase
            #total = (symbol) * shares
           # if user_account.balance >= total:


           # Deduct the amount from the user's account

                #request.user.account_balance -= total
                #request.user.save()
               
            # Record the transaction
            #transaction = Transaction.objects.create(
            #user=request.user,
            #symbol=symbol,
            #shares=shares,
            #price=price,
            #total=total
            #)

            # Render a confirmation message
            #messages.success(request, f"Stocks bought successfully! Transaction ID: {transaction.id}")
            return render(request, 'userside/confirmation2.html',  {'stock_data': stock_data})  # Redirect to the user's dashboard or any other relevant page
            # else:
            #messages.error(request, "Insufficient funds. Cannot complete the purchase.")
        else:
                messages.error(request, "Invalid input. Please check your input and try again.")
    else:
        form = SellStockForm()
    return render(request, 'userside/sell_stocks.html', {'form': form})



# portfolio & transaction views 

def portfolio(request):
    user = request.user
    portfolio = Portfolio.objects.all()
    transactions = Transaction.objects.filter(user=user)
    stock_data = Stocks.objects.all()

    # Calculate the total portfolio value
    #total_value = portfolio.cash_balance

    holdings = []
    #for transaction in transactions:
       # stock = transaction.stock
       # shares = transaction.shares
       # price = get_stock_price(stock.symbol) # call the lookup function for stock prices
       # value = shares * price
       # total_value += value

       # holdings.append9({
        #    'stock': stock,
        #    'shares': shares,
        #    'price' : price,
        #    'value' : value,
       # })
    context = {
        'portfolio': portfolio,
        'holdings': holdings,
        # 'total_value': total_value,
    }

    return render(request, 'userside/portfolio.html', {'stock_data': stock_data})



def transaction_history(request):
    transactions = Transaction.objects.all()
    return render(request, 'userside/transaction_history.html', {'transactions': transactions})



