from django.urls import path
from . import views

urlpatterns = [
    path('second_price_auction/', views.second_price_auction, name='second_price_auction'),
]
