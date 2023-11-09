# stock_quote/views.py
import requests
from django.shortcuts import render
from .forms import StockQuoteForm

def get_stock_quote(request):
    if request.method == 'POST':
        form = StockQuoteForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            
            # Make a request to the IEX Cloud API to get the stock price
            api_token = 'sk_f5db8502ccae44cea64f3ab923edfdcf'
            api_url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={api_token}'
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                stock_price = data['latestPrice']
                return render(request, 'stock_quote/quoted.html', {'symbol': symbol, 'stock_price': stock_price})
            else:
                error_message = 'Failed to fetch stock data. Please check the symbol and try again.'
                return render(request, 'stock_quote/quote.html', {'form': form, 'error_message': error_message})
    else:
        form = StockQuoteForm()
        return render(request, 'stock_quote/quote.html', {'form': form})