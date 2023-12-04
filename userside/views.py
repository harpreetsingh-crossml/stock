from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
from .models import StockSell, Stock, UserProfile, Transaction
from .models import Portfolio
from .forms import BuyStockForm, SellStockForm
from .utils import get_stock_price
import requests

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Transaction
from stock_quote.models import Stocks

# log in & log out views

def index(request):
     return render(request,"userside/index.html")

def index2(request):
     return render(request,"userside/index2.html")



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
    if request.method == 'POST':
        form = BuyStockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            shares = form.cleaned_data['shares']
            total = form.cleaned_data['total']
            stock_data = Stocks.objects.filter(price=price)
            total = price * shares ; {'stock_data': stock_data}
                    # user = request.user
                    #  user_account = UserProfile.objects.get(user=user)

                        # Check if the user can afford the purchase
                       # purchase_price = get_stock_price(symbol) * shares
                        #if user_account.balance >= purchase_price:
                            # Deduct the purchase amount from the user's account
                        #    user_account.balance -= purchase_price
                        #  user_account.save()
                        
                            # Record the transaction in the database
                      #  Stocks.objects.create(
                               
                            #    symbol=symbol,
                             #   shares=shares,
                             #   total=total
                          #  )

            return render(request, 'userside/confirmation.html', {'message': 'Stock purchased successfully!'})
        else:
            return render(request, 'userside/apology.html', {'message': 'Insufficient funds!'})

    else:
        form = BuyStockForm()

    return render(request, 'userside/buy_stocks.html', {'form': form})


# sell stocks


def sell_stock(request):
    
    if request.method == 'POST':
        form = SellStockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            shares = form.cleaned_data['shares']
           # price = request.POST['price']
           # total_amount = price * shares
            
            # Check if the user can afford the purchase
            if total_amount <= request.user.account_balance:
                      # Deduct the amount from the user's account
                    #  request.user.account_balance -= total_amount
                    # request.user.save()
               
                    # Record the transaction
                     # transaction = Stocks.objects.create(
                    #    user=request.user,
                        # symbol=symbol,
                     #   shares=shares,
                       # price=price,
                      #  total_amount=total_amount
                    #)

                    # Render a confirmation message
                messages.success(request, f"Stocks bought successfully! Transaction ID: {transaction.id}")
                return redirect(request, 'userside/confirmation.html')  # Redirect to the user's dashboard or any other relevant page
            else:
             messages.error(request, "Insufficient funds. Cannot complete the purchase.")
        else:
                messages.error(request, "Invalid input. Please check your input and try again.")
    else:
        form = SellStockForm()
    return render(request, 'userside/sell_stocks.html', {'form': form})



# portfolio & transaction views 

def portfolio(request):
    user = request.user
    #portfolio = Portfolio.objects.get(user=user)
    transactions = Transaction.objects.filter(user=user)

    # Calculate the total portfolio value
    #total_value = portfolio.cash_balance

    holdings = []
    for transaction in transactions:
        stock = transaction.stock
        shares = transaction.shares
        price = get_stock_price(stock.symbol)  # Call the lookup function for stock prices
        value = shares * price
        total_value += value

        holdings.append({
            'stock': stock,
            'shares': shares,
            'price': price,
            'value': value,
        })

    context = {
        'portfolio': portfolio,
        'holdings': holdings,
       # 'total_value': total_value,
    }

    return render(request, 'userside/portfolio.html', context)


def transaction_history(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user).order_by('-date_time')
    return render(request, 'userside/transaction_history.html', {'transactions': transactions})


#def sell_stock(request):
    symbol = UserProfile.objects.get(user=request.user)
    stocks = Stock.objects.all()

    if request.method == 'POST':
        stock_symbol = request.POST['stock']
        shares_to_sell = int(request.POST['shares'])

        stock = get_object_or_404(Stock, symbol=stock_symbol)
        user_balance = user_profile.balance

        if user_balance >= stock.current_price * shares_to_sell:
            # Update user balance
            user_profile.balance -= stock.current_price * shares_to_sell
            user_profile.save()

            # Record the sale transaction
            Transaction.objects.create(
                user=request.user,
                stock=stock,
                shares=shares_to_sell,
                price=stock.current_price
            )

            return render(request, 'confirmation.html', {'message': 'Stock sold successfully.'})
        else:
            return render(request, 'confirmation.html', {'message': 'Insufficient funds.'})

    return render(request, 'sell_stock.html', {'stocks': stocks})




#def sell_stock(request):
    form = SellStockForm(request.POST)
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
    return render(request, 'userside/sell_stocks.html', {'stocks': stocks})

