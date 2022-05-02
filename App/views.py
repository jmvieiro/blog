from django.http import HttpResponse

from .models import Curso

def curso(self):
    curso = Curso(nombre = "Curso de Python", camada = 1)
    curso.save()
    texto = f"Curso creado {curso.nombre} - camada {curso.camada}"
    return HttpResponse(texto)