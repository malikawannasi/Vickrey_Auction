from django.http import JsonResponse
from .models import Bid


def second_price_auction(request):
    # Sample Input: Reserve Price and Bids (can be passed via POST or hardcoded for now)
    reserve_price = float(request.GET.get('reserve_price', 100))
    bids = list(Bid.objects.all().values('bidder_name', 'bid_amount'))

    # Filter bids above the reserve price
    valid_bids = [bid for bid in bids if bid['bid_amount'] >= reserve_price]
    if not valid_bids:
        return JsonResponse({"winner": None, "winning_price": reserve_price})

    # Sort bids by amount in descending order
    sorted_bids = sorted(valid_bids, key=lambda x: x['bid_amount'], reverse=True)

    # Determine the winner and the winning price
    winner = sorted_bids[0]['bidder_name']
    second_highest_bid = sorted_bids[1]['bid_amount'] if len(sorted_bids) > 1 else reserve_price

    # Output result
    return JsonResponse({
        "winner": winner,
        "winning_price": second_highest_bid
    })
