from socket import fromshare
from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=50, label="Título")
    subtitle = forms.CharField(max_length=100, label="Subtítulo")
    content = forms.CharField(widget=forms.Textarea, label="Contenido")
    
class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre")
    last_name = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(label="Email")
    topic = forms.CharField(max_length=100, label="Especialidad")

class TopicForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre")
