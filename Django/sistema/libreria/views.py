from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.


def inicio(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def listar(request):
    libros = Libro.objects.all()
    return render(request, "libros/index.html", {'libros': libros})

def crear(request): 
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, "libros/crear.html", {'formulario': formulario})

def editar(request):
    return render(request, "libros/editar.html")

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')