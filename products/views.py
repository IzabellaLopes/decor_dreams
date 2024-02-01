"""Products Views"""

from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to show all products, sorting and search functionality """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
