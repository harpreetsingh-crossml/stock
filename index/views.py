import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PortfolioItem
from .models import Transaction

# Create your views here.

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