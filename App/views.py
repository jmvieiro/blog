from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

def index(request):
    return render(request, "index.html")

def profesores(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        profesion = request.POST.get("profesion")
        profesor = Profesor(nombre = nombre, apellido = apellido, email = email, profesion = profesion)
        profesor.save()
        texto = f"Profesor creado {profesor.nombre} - {profesor.apellido} - {profesor.email} - {profesor.profesion}"
        return render(request, "profesores.html", {"texto": texto})
    return render(request, "profesores.html")

def estudiantes(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        carrera = request.POST.get("carrera")
        estudiante = Estudiante(nombre = nombre, apellido = apellido, email = email, carrera = carrera)
        estudiante.save()
        texto = f"Estudiante creado {estudiante.nombre} - {estudiante.apellido} - {estudiante.email} - {estudiante.carrera}"
        return render(request, "estudiantes.html", {"texto": texto})
    return render(request, "estudiantes.html")

def cursos(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        camada = request.POST.get("camada")
        curso = Curso(nombre = nombre, camada = camada)
        curso.save()
        texto = f"Curso creado {curso.nombre} - camada {curso.camada}"   
        return render(request, "cursos.html", {"texto": texto})
    return render(request, "cursos.html")
