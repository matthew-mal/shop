from django.shortcuts import render
from cart.core import Cart
from order.forms import OrderForm


def order(request):
    cart = Cart(request)
    if request.method == 'GET':
        orders = OrderForm()
        return render(request, 'order_details.html', {'orders': orders, 'cart': cart})
    else:
        orders = OrderForm(request.POST)
        if orders.is_valid():
            orders.save()
            cart.clear()
        return render(request, 'successful_order.html')

