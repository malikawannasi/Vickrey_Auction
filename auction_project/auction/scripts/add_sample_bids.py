from auction.models import Bid

def run():
    Bid.objects.create(bidder_name="A", bid_amount=110)
    Bid.objects.create(bidder_name="A", bid_amount=130)
    Bid.objects.create(bidder_name="C", bid_amount=125)
    Bid.objects.create(bidder_name="D", bid_amount=105)
    Bid.objects.create(bidder_name="D", bid_amount=115)
    Bid.objects.create(bidder_name="E", bid_amount=132)
    Bid.objects.create(bidder_name="E", bid_amount=140)
    print("Sample bids added successfully!")

