from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0

    if 'admin' in request.path:
        return {}

    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart__in=cart)

        for cart_item in cart_items:
            cart_count += cart_item.quantity

    except Exception:
        cart_count = 0

    return dict(cart_count=cart_count)
