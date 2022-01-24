from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey
from django.forms import model_to_dict, forms


class Usuarios(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    nickname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    passwork=models.CharField(max_length=50)

    def __str__(self):
        return self.name + self.lastname

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-id']

