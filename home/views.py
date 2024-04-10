"""Home Views"""

from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """

    top_products = Product.objects.filter(is_top_product=True)[:6]

    context = {
        'top_products': top_products,
    }

    return render(request, 'home/index.html', context)