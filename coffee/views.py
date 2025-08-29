from django.shortcuts import render, redirect, get_object_or_404
from .models import Coffee, CartItem


def home(request):
    hot_coffees = Coffee.objects.filter(category='hot')
    cold_coffees = Coffee.objects.filter(category='cold')
    special_coffees = Coffee.objects.filter(category='special')

    return render(request, 'home.html', {
        'hot_coffees': hot_coffees,
        'cold_coffees': cold_coffees,
        'special_coffees': special_coffees,
    })


def view_cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.get_total() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


def add_to_cart(request, product_id):
    coffee_item = get_object_or_404(Coffee, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=coffee_item)
    if not created:
        cart_item.quantity += 1   # fixed (lowercase 'quantity')
        cart_item.save()
    return redirect('view_cart')


def update_quantity(request, cart_id, action):  # fixed spelling
    cart_item = get_object_or_404(CartItem, id=cart_id)

    if action == "increase":
        cart_item.quantity += 1   # fixed
        cart_item.save()
    elif action == "decrease":
        if cart_item.quantity > 1:
            cart_item.quantity -= 1   # fixed
            cart_item.save()
        else:
            cart_item.delete()
    return redirect("view_cart")

    
    