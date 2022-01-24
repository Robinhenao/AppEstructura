from config.wsgi import *
from foro.models import Categoria

categorias = Categoria.objects.all()
print(type(categorias))

'''
categoria = Categoria(nombre="Python 3")
categoria.save()
'''
categoriaPython = Categoria.objects.get(pk=1)
print(categoriaPython)