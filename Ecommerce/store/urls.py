from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
   path('', views.index, name='home'),
   path('cart/', views.cart, name='cart'),
   path('checkout/', views.checkout, name='checkout'),
]
