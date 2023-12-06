from django.contrib import admin
from userside.models import Stock


# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol','price')
admin.site.register(Stock,StockAdmin)
