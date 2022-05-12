from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("authors/create", create_author, name="create_author"),
    path("authors/get", get_author, name="get_author"),
    path("posts/create", create_post, name="create_post"),
    path("post/get", get_post, name="get_post"),
    path("topics/create", create_topic, name="create_topic"),
    path("topics/get", get_topic, name="get_topic"),
    path("register/", register, name="register"),
]
