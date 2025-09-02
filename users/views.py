from django.shortcuts import render
from django.http import HttpResponse

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
