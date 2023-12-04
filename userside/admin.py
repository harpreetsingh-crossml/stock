from django.contrib import admin
from .models import Stock


# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol','price')

    def get_price(self, obj):
        return obj.price
     get_price.short_description = 'price'
    
admin.site.register(Stock,StockAdmin)