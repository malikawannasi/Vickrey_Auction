import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction_project.settings')
django.setup()


from django.test import TestCase
from auction.models import Bid


class AuctionTestCase(TestCase):
    def setUp(self):
        Bid.objects.create(bidder_name="Alice", bid_amount=150)
        Bid.objects.create(bidder_name="Bob", bid_amount=200)

    def test_second_price_auction(self):
        response = self.client.get('/auction/second_price_auction/?reserve_price=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['winner'], "Bob")
        self.assertEqual(response.json()['winning_price'], 150)
