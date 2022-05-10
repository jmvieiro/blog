from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("authors/create", create_author, name="create_author"),
    path("authors/delete/<id>", delete_author, name="delete_author"),    
    path("posts/create", create_post, name="create_post"),
    path("posts/delete/<id>", delete_post, name="delete_post"),
    path("topics/create", create_topic, name="create_topic"),
    path("topics/delete/<id>", delete_topic, name="delete_topic"),
    path("register/", register, name="register"),

]
