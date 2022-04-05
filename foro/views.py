from django.shortcuts import render, redirect
from foro.forms import FormularioPost
from django.contrib import messages
from foro.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def foro(request):
    listado_posts = Post.objects.all()
    paginator = Paginator(listado_posts, 3)
    pagina = request.GET.get("page") or 1
    posts = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, posts.paginator.num_pages + 1)
    return render(request, "foro.html", {"posts": posts, "paginas": paginas, "pagina_actual": pagina_actual})


def make_post(request):
    if request.method == "POST":
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor_id = request.user.id
            post.save()

            titulo = form.cleaned_data.get("titulo")
            messages.success(request, f" Se posteo {titulo} correctamente")
            return redirect("foro")
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])

    form = FormularioPost()
    return render(request, "make_post.html", {"form": form})


def delete_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        messages.error(request, "el post a eliminar no existe")
        return redirect("foro")

    if post.autor != request.user:
        messages.error(request, "no eres el autor")
        return redirect("foro")

    post.delete()
    messages.success(request, f"el post {post.titulo} ha sido eliminado")
    return redirect("foro")


def show_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'show_post.html',{'show_post':post})
