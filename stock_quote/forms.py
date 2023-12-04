from django import forms 


class StockQuoteForm(forms.Form):
   symbol = forms.CharField(label='Stock Symbol', max_length=10)
   