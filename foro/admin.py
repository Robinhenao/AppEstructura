from django.contrib import admin
from foro.models import Categoria,Post

admin.site.register([Categoria,Post])