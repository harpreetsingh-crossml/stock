from django.urls import path
from . import views

urlpatterns = [
    path('buy-stock/', views.buy_stock, name='buy-stock'),
    path('sell-stock/', views.sell_stock, name='sell-stock'),
]