from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .core import Cart
from .forms import CartAddProductForms
from store.models import Product


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})


@require_POST
def cart_add(request, pr_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pr_id)
    form = CartAddProductForms(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, pr_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pr_id)
    cart.remove(product)
    return redirect('cart_detail')
