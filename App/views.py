from django.http import HttpResponse
from django.shortcuts import render

from .models import Curso

# def curso(request):
#     curso = Curso(nombre = "Curso de Python", camada = 1)
#     curso.save()
#     texto = f"Curso creado {curso.nombre} - camada {curso.camada}"
#     return HttpResponse(texto)


def index(request):
    return render(request, "index.html")

def profesores(request):
    return HttpResponse("Hola profesores")

def estudiantes(request):
    return HttpResponse("Hola estudiantes")

def cursos(request):
    return HttpResponse("Hola cursos")

def entregables(request):
    return HttpResponse("Hola entregables")