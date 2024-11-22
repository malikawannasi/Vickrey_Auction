from django.db import models

class Bid(models.Model):
    bidder_name = models.CharField(max_length=50)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.bidder_name}: {self.bid_amount}"
