from django import forms

class StockPurchaseForm(forms.Form):
    stock_symbol = forms.CharField(label='Stock Symbol', max_length=10)
    shares = forms.IntegerField(label='Number of Shares')