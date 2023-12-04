from django.contrib import admin
from django.urls import include, path
from userside import views
from .views import portfolio
from . import views


app_name = "userside"
urlpatterns = [
# login logout urls
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('index2/', views.index2, name="index2"),
    
    path('user-register/', views.user_register, name="user-register"),
    path('user-login/', views.user_login, name="user-login"),
    path('logout/', views.user_logout, name="logout"),
    path('banner/', views.banner_image, name='banner'),
   
# sell buy urls
    path('buy-stock/', views.buy_stock, name='buy-stock'),
    path('sell-stock/', views.sell_stock, name='sell-stock'),

# portfolio & transaction
    path('portfolio/', views.portfolio, name='portfolio'),
    path('transaction-history/', views.transaction_history, name='transaction-history'),


]