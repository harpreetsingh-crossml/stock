from django import forms

class BuyStockForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=10)
    shares = forms.IntegerField(label='No. of Shares to Buy', min_value=1)
    total = forms.DecimalField(label='Total Price', max_digits=10, decimal_places=2)


class SellStockForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=10)
    shares = forms.IntegerField(label='No. of Shares to Sell', min_value=1) 
    total = forms.IntegerField(label='Total', max_value=40)