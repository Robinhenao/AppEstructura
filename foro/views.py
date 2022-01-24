from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from foro.forms import FormularioPost

def foro(request):
    return render(request,"foro.html")


def make_post(request):
    form = FormularioPost()
    return render(request,"make_post.html",{"form":form})
