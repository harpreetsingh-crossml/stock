from django.contrib import admin
from stock_quote.models import Stocks

class StocksAdmin(admin.ModelAdmin):
    list_display=( 'name','symbol','available_shares','price',)

admin.site.register(Stocks,StocksAdmin)