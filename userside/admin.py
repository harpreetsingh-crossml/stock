from django.contrib import admin
from userside.models import Stock
from userside.models import Transaction


# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol','price')
admin.site.register(Stock,StockAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('symbol','shares','price','transaction_type','date_time')
admin.site.register(Transaction,TransactionAdmin)