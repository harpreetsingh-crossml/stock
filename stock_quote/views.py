# stock_quote/views.py
import requests
from django.shortcuts import render, redirect
from .forms import StockQuoteForm
from .models import Stocks
from  django.conf import settings


def quote(request):
    if request.method == 'POST':
        form = StockQuoteForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            # Fetch dummy stock data from the database
            stock_data = Stocks.objects.get(symbol=symbol)
           
            return render(request, 'stock_quote/quoted.html', {'stock_data': stock_data})
    else:
        form = StockQuoteForm()
    return render(request, 'stock_quote/quote.html', {'form': form})
    


def stock_home(request):
    return render(request,"stock_quote/stock_home.html")