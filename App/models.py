from turtle import title
from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title  = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    ts_created = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    topic = models.CharField(max_length=100)
    def __str__(self):
        return self.name + " " + self.last_name + " " + self.topic
