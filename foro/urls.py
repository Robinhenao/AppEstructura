from django.urls import path
from .views import *

urlpatterns = [
    path('', foro, name="foro"),
    path('post/make', make_post, name="make_post"),
    path('post/delete/<int:post_id>', delete_post, name="delete_post"),
]