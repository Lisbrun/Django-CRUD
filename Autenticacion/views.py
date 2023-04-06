from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from  django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

class signup(View):
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            User=form.save()
            login(request,User)
            return redirect('Taks')
        else:
            return HttpResponse('Usuario ya existente')

    def get(self, request):
        form = CreateUserForm()
        return render(request, 'Autenticacion/signup.html', {'form': form})

@login_required(login_url='/Autenticacion/login')
def salir(request):
    logout(request)
    return redirect('Principal')


def loguearse(request):
    if request.method =="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre= form.cleaned_data.get('username')
            contraseña= form.cleaned_data.get('password')
            Usuario= authenticate(request,username=nombre,password=contraseña)
            if Usuario is not None:
                login(request,Usuario)
                return redirect('Principal')
            else:
                messages.error(request,'Error al validar la peticion')

    form= AuthenticationForm()
    return render(request,'Autenticacion/login.html',{"form":form})