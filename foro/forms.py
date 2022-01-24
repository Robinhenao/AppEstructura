from django import forms
from .models import Post

class FormularioPost(forms.ModelForm):
    class meta:
        model= Post
        fields = ('categoria','titulo','contenido','imagen')
