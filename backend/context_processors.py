from .cart import Cart
from .forms import CartForm

def cart(request):
    return {'cart': Cart(request)}


