from django.contrib import admin

from userside.models import Transaction


# Register your models here.



class TransactionAdmin(admin.ModelAdmin):
    list_display = ('symbol','shares','price','transaction_type','date_time')
admin.site.register(Transaction,TransactionAdmin)