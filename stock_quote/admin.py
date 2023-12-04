from django.contrib import admin
from stock_quote.models import Stocks

class StocksAdmin(admin.ModelAdmin):
    list_display=( 'symbol','price',)

# Register your models here.
admin.site.register(Stocks,StocksAdmin)