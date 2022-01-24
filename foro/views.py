from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
class loginUsuarioView(HttpRequest):
    def base(request):
        return render(request,"base.html")


def registro(request):
        return render(request,"registro.html")