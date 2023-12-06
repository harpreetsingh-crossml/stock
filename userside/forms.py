from django import forms

class BuyStockForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=10)
    shares = forms.IntegerField(label='No. of Shares to Buy', min_value=1)

class SellStockForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=10)
    shares = forms.IntegerField(label='No. of Shares to Sell', min_value=1) 
 