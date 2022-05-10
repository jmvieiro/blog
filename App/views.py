from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *

def index(request):
    authors = Author.objects.all()
    posts = Post.objects.all()
    topics = Topic.objects.all()
    context = {"authors": authors, "posts": posts, "topics": topics}
    return render(request, "index.html", context)

def register(request):
    return render(request, "register.html")

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        content = request.POST.get("content")
        posts = Post(title = title, subtitle = subtitle, content = content)
        posts.save()
        return redirect("index")
    return redirect("index")

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("index")

def create_author(request):
    if request.method == "POST":
        name = request.POST.get("name").upper()
        last_name = request.POST.get("last_name").upper()
        email = request.POST.get("email")
        topic = request.POST.get("topic")
        author = Author(name = name, last_name = last_name, email = email, topic = topic)
        author.save() 
        return redirect("index")
    return redirect("index")

def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect("index")

def create_topic(request):
    if request.method == "POST":
        name = request.POST.get("name")
        topic = Topic(name = name)
        topic.save()
        return redirect("index")
    return redirect("index")

def delete_topic(request, id):
    topic = Topic.objects.get(id=id)
    topic.delete()
    return redirect("index")