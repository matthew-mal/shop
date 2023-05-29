from decimal import Decimal
from django.conf import settings
from store.models import Product


class Cart(object):
    # Initializing the shopping cart
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CARD_SESSION_ID)
        if not cart:
            # Saving an empty card in the session
            cart = self.session[settings.CARD_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        # Add a product to cart or update its quantity
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Update cart session
        self.session[settings.CARD_SESSION_ID] = self.cart
        # Mark session as modified to see that it is saved
        self.session.modified = True

    def remove(self, product):
        # Deleting an item from the shopping cart
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        # Search through items from the shopping cart and get products from the database
        self.products_ids = self.cart.keys()

        # Get the product object and put it in the cart
        products = Product.objects.filter(id__in=self.products_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Counting the number of products
        return sum(item['quantity'] for item in self.cart.values())

    def total_price(self):
        # Calculating the price of products in the shopping cart
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # delete cart from session
        del self.session[settings.CARD_SESSION_ID]
        self.session.modified = True
