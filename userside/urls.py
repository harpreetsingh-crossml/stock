from django.contrib import admin
from django.urls import include, path
from userside import views
from . import views


app_name = "userside"
urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('user-register/', views.user_register, name="user-register"),
    path('user-login/', views.user_login, name="user-login"),
    path('logout/', views.user_logout, name="logout"),
    path('banner/', views.banner_image, name='banner'),
   

]