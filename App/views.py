from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect

from App.forms import AuthorForm, PostForm, TopicForm

from .models import *


def index(request):
    authors = Author.objects.all()
    posts = Post.objects.all()
    topics = Topic.objects.all()
    context = {"authors": authors, "posts": posts, "topics": topics}
    return render(request, "index.html", context)


def register(request):
    authorForm = AuthorForm()
    postForm = PostForm()
    topicForm = TopicForm()
    return render(request, "register.html", {"authorForm": authorForm, "postForm": postForm, "topicForm": topicForm})


def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        title = data.get("title")
        subtitle = data.get("subtitle")
        content = data.get("content")
        post = Post(title=title, subtitle=subtitle, content=content)
        post.save()
    return redirect("index")


def create_author(request):
    form = AuthorForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        name = data.get("name").upper()
        last_name = data.get("last_name").upper()
        email = data.get("email")
        topic = data.get("topic")
        author = Author(name=name, last_name=last_name,
                        email=email, topic=topic)
        author.save()
    return redirect("index")


def create_topic(request):
    form = TopicForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        name = data.get("name")
        topic = Topic(name=name)
        topic.save()
    return redirect("index")


def get_author(request):
    if request.GET.get("authorId"):
        id = request.GET.get("authorId")
        try:
            author = Author.objects.get(id=request.GET.get("authorId"))
            return render(request, "result.html", {"author": author})
        except Author.DoesNotExist:
            return render(request, "result.html", {"response": f"No existe autor para el ID #{id} ingresado."})
    return render(request, "result.html", {"response": "No se ingresó el ID del autor."})


def get_post(request):
    if request.GET.get("postId"):
        id = request.GET.get("postId")
        try:
            post = Post.objects.get(id=request.GET.get("postId"))
            return render(request, "result.html", {"post": post})
        except Post.DoesNotExist:
            return render(request, "result.html", {"response": f"No existe post para el ID #{id} ingresado."})
    return render(request, "result.html", {"response": "No se ingresó el ID del post."})


def get_topic(request):
    if request.GET.get("topicId"):
        id = request.GET.get("topicId")
        try:
            topic = Topic.objects.get(id=request.GET.get("topicId"))
            return render(request, "result.html", {"topic": topic})
        except Topic.DoesNotExist:
            return render(request, "result.html", {"response": f"No existe tema para el ID #{id} ingresado."})
    return render(request, "result.html", {"response": "No se ingresó el ID del tema."})
