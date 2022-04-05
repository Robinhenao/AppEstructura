from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
import os

class Categoria(models.Model):
    nombre= models.CharField(max_length=100,null=False,unique=True,verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class meta:
        db_table="categories"
        verbose_name="Categoria"
        verbose_name_plural = "Categorias"
        ordering=['id']


class Post(models.Model):
    autor= models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100,unique=True,null=False ,verbose_name='Titulo')
    contenido= models.TextField(null=True,verbose_name='Contenido post')
    imagen = models.ImageField(upload_to='posts/%Y/%m/%d',null=True,blank=True,verbose_name='Imagen post')
    fecha_alta = models.DateTimeField(auto_now_add=True,verbose_name='Fecha alta')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha actualizacion')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
            super(Post,self).delete(*args,**kwargs)

    def __str__(self):
        return self.titulo

    class meta:
        db_table="posts"
        verbose_name="Post"
        verbose_name_plural = "Posts"
        ordering=['id']