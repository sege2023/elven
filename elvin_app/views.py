from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, Product, OrderItem

# Create your views here.
def home(request):
    return render(request, 'index.html')



def products(request, category):
    # category = request.GET.get('category')
    items = Product.objects.filter(category__name=category)
    return render(request, "products.html", {"products": items})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    return render(request, 'cart.html', {'items': items, 'order': order})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    return render(request, 'checkout.html', {'items': items, 'order': order})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    customer = request.user.customer
    order, _ = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(product=product, order=order)
    orderitem.quantity += 1
    orderitem.save()

    return redirect('products', category=product.category.name)


def increase_count(request, orderitem_id):
    orderitem = OrderItem.objects.get(id=orderitem_id)
    orderitem.quantity += 1
    orderitem.save()

    return redirect('cart')


def decrease_count(request, orderitem_id):
    orderitem = OrderItem.objects.get(id=orderitem_id)
    orderitem.quantity -= 1
    orderitem.save()

    return redirect('cart')