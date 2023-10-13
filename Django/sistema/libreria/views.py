from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def libros(request):
    return render(request, "libros/index.html")