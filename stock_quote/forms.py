from django import forms 


class StockQuoteForm(forms.Form):
    symbol = forms.CharField(max_length=10, label='Enter Stock Symbol')