from django.urls import path
from . import views
from .views import quote


app_name = "stock_quote"

urlpatterns = [
    path('quote/', views.quote, name='quote'),
    path('stock-home/', views.stock_home, name="stock-home"),
]