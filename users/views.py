from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import Product
from django.urls import reverse_lazy

# Create your views here.

def test_view(request):
    return HttpResponse("<h1>¡Hola! Esta es una vista de prueba.</h1>")


def home(request):
    user = request.user
    context = {
        'title': 'Proyecto 2025',
        'message': 'Bienvenido al proyecto de prueba'
    }
    return render(request, 'home.html', context)

def welcome(request):
    return render(request, "base.html")

def about(request):
    context ={
        "products": Product.objects.filter(
            is_active=True
        )
    }
    return render(
        request,
        "about.html",
        context=context
    )

def create_product(request):
    if request.method == "GET":
        return render(
            request,
            "product/create.html",
        )
    else:
        product = Product()
        product.name = request.POST['name_product']
        product.stock = request.POST['stock_product']
        product.save()
        return redirect(reverse_lazy("about"))

def update_product(request):
    pass

def delete_product(request):
    pass
