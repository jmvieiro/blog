from django.contrib import admin

from App.models import *

# Register your models here.

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Author)