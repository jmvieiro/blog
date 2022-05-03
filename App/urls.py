from django.urls import path
from .views import *

urlpatterns = [
    # path("", list_persons, name="list_persons"),
    path("", index),
    path("profesores/", profesores),
    path("estudiantes/", estudiantes),
    path("cursos/", cursos),
    path("entregables/", entregables),
]
