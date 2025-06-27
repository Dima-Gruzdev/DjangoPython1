from django.shortcuts import render

from catalog.models import Product


def home(requests):
    products = Product.objects.all()
    if requests.method == 'GET':
        return render(requests, 'home.html', {'products': products})


def contacts(requests):
    if requests.method == 'GET':
        return render(requests, 'contacts.html')


def product_detail(requests, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(requests, 'product_detail.html', context)
