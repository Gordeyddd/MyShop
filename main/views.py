from django.shortcuts import render, get_object_or_404
from unicodedata import category

from .models import *


def main (request):
    query = request.GET.get('q', '')
    products = Product.objects.order_by('price')
    cat = request.GET.get('c', '')
    if query:
        products = products.filter(name__icontains=query)
    if cat:
        products = products.filter(category_id=cat)
    context = {
        'product': products,
        'category': Category.objects.all(),
        'query': query,
        'cat' : cat,
    }
    return render(request, 'main.html', context)


def detail (request, slug):
    product = get_object_or_404(Product, slug= slug)
    return render(request, 'detail.html', {'product' : product})