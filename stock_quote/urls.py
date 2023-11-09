from django.urls import path
from .views import get_stock_quote
from . import views
from stock_quote.views import get_stock_quote

urlpatterns = [
    path('quote/', views.get_stock_quote, name='quote'),
]