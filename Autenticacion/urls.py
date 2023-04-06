
from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signup.as_view(), name='Signup'),
    path('salir/', salir, name='Salir'),
    path('login/',loguearse, name="login"),

]