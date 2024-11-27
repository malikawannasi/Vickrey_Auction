from django.db import models

class Bid(models.Model):
    bidder_name = models.CharField(max_length=100)
    bid_amount = models.FloatField()

    def __str__(self):
        return f"{self.bidder_name}: {self.bid_amount}"

