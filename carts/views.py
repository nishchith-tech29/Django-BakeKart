from django.shortcuts import get_object_or_404, render 
from .models import Cart, CartItem
from store.models import Product , Variation
from django.shortcuts import redirect

def cart(request,total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (5 * total)/100
        grand_total = total + tax
    except Cart.DoesNotExist:
        pass # just ignore
    return render(request, 'store/cart.html', {'total': total, 'quantity': quantity, 'cart_items': cart_items,'tax': tax, 'grand_total': grand_total})
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_variation = []

    if request.method == 'POST':
        for key, value in request.POST.items():
            try:
                variation = Variation.objects.get(
                    product=product,
                    variation_category__iexact=key,
                    variation_value__iexact=value
                )
                product_variation.append(variation)
            except Variation.DoesNotExist:
                continue

    cart, created = Cart.objects.get_or_create(
        cart_id=_cart_id(request)
    )

    cart_items = CartItem.objects.filter(
        product=product,
        cart=cart,
        is_active=True
    )

    ex_var_list = []
    id_list = []

    for item in cart_items:
        existing_variations = item.variations.all()
        ex_var_list.append(
            sorted(v.id for v in existing_variations)
        )
        id_list.append(item.id)

    selected_variations = sorted(
        v.id for v in product_variation
    )

    if selected_variations in ex_var_list:
        index = ex_var_list.index(selected_variations)
        item_id = id_list[index]

        item = CartItem.objects.get(id=item_id)
        item.quantity += 1
        item.save()

    else:
        item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )

        if product_variation:
            item.variations.set(product_variation)

        item.save()

    return redirect('cart')

    
    product = get_object_or_404(Product, id=product_id)
    product_variation = []

    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(
                    product=product,
                    variation_category__iexact=key,
                    variation_value__iexact=value
                )
                product_variation.append(variation)
            except Variation.DoesNotExist:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )

        is_cart_item_exists = CartItem.objects.filter(
            product=product,
            cart=cart
        ).exists()

        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(
                product=product,
                cart=cart
            )

            ex_var_list = []
            id = []

            for item in cart_item:
                existing_variations = item.variations.all()
                ex_var_list.append(list(existing_variations))
                id.append(item.id)

            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(
                    product=product,
                    id=item_id
                )
                item.quantity += 1
                item.save()

            else:
                item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    cart=cart
                )

                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)

                item.save()

        else:
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart
            )

            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)

            cart_item.save()

    else:
        is_cart_item_exists = CartItem.objects.filter(
            product=product,
            cart=cart
        ).exists()

        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(
                product=product,
                cart=cart
            )

            ex_var_list = []
            id = []

            for item in cart_item:
                existing_variations = item.variations.all()
                ex_var_list.append(list(existing_variations))
                id.append(item.id)

            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(
                    product=product,
                    id=item_id
                )
                item.quantity += 1
                item.save()

            else:
                cart_item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    cart=cart
                )

                if len(product_variation) > 0:
                    cart_item.variations.clear()
                    cart_item.variations.add(*product_variation)

                cart_item.save()

        else:
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart
            )

            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)

            cart_item.save()

    return redirect('cart')




def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)

    cart_item = CartItem.objects.filter(
        product=product,
        cart=cart,
        is_active=True
    ).first()

    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)

    cart_item = CartItem.objects.filter(
        product=product,
        cart=cart,
        is_active=True
    ).first()

    if cart_item:
        cart_item.delete()

    return redirect('cart')
