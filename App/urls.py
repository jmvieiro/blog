from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("cursos/", cursos, name="cursos"),
]
