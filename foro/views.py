from django.shortcuts import render, redirect
from foro.forms import FormularioPost
from django.contrib import messages
from foro.models import Post
from django.core.paginator import Paginator

def foro(request):
    listado_posts = Post.objects.all()
    paginator = Paginator(listado_posts,3)
    pagina = request.GET.get("page") or 1
    posts = paginator.get_page(pagina)
    pagina_page= int(pagina)
    paginas = range(1,posts.paginator.num_pages+1)
    return render(request,"foro.html",{"posts":posts ,"paginas":paginas,"pagina_actial":pagina_page})


def make_post(request):
    if request.method =="POST":
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor_id = request.user.id
            post.save()
            titulo =form.cleaned_data.get("titulo")
            messages.success(request,f" Se posteo {titulo} correctamente")
            return redirect("foro")
        else:
            for msg in form.error_message:
                messages.error(request,form.error_messages[msg])

    form = FormularioPost()
    return render(request,"make_post.html",{"form":form})
