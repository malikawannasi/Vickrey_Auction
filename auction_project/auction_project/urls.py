from django.urls import path
from auction.views import second_price_auction  # Utilisez le chemin correct ici
from auction import views  # Import the whole views module

urlpatterns = [
    path('', second_price_auction, name='second_price_auction'),
]
