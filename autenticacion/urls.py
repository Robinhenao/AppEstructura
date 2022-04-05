from django.urls import path
from .views import viewRegistro, logoutSession, loginsession

urlpatterns = [
    path('registro/', viewRegistro.as_view(), name="registro"),
    path('login/', loginsession, name="login"),
    path('logoutsession/', logoutSession, name="logoutsession"),
]
