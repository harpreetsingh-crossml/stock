from django.contrib import admin

from userside.models import Transaction
from userside.models import UserProfile
from userside.models import Portfolio

# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user','symbol','shares','price','transaction_type','date_time')
admin.site.register(Transaction,TransactionAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','account_balance')
admin.site.register(UserProfile,UserProfileAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user','symbol','shares','price','total')
admin.site.register(Portfolio,PortfolioAdmin)

