from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def favorites_contents(request):
    """ context docstring """

    favorites_items = []
    total = 0
    favorites = request.session.get('favorites', {})

    for item_id, item_data in favorites.items():
            product = get_object_or_404(Product, pk=item_id)
            favorites_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    context = {
        'favorites_items': favorites_items,
    }

    return context
