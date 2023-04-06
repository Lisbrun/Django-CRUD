from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from .forms import formTask
from .models import taks
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def Home(request):
    return render(request, 'Home.html')

@login_required(login_url='/Autenticacion/login')
def tasks(request):
    info = taks.objects.filter(User=request.user, Datecompleted__isnull=True)
    return render(request, 'taks.html', {'info': info})

@login_required(login_url='/Autenticacion/login')
def createTask(request):
    if request.method == "POST":
        form = formTask(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.User = request.user
            info.save()
            return redirect('Taks')

    form = formTask()
    return render(request, 'createTask.html', {'form': form})

@login_required(login_url='/Autenticacion/login')
def task_detail(request, task_id):
    if request.method == "POST":
        tarea = get_object_or_404(taks, pk=task_id, User=request.user)
        form = formTask(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Creado Correctamente ')
            return redirect('Taks')

        else:
            messages.warning(request, " error al crear la peticion")
    info = get_object_or_404(taks, pk=task_id, User=request.user)
    form = formTask(instance=info)
    return render(request, 'task_detail.html', {'info': info, 'form': form})

@login_required(login_url='/Autenticacion/login')
def completetask(request, task_id):
    tarea = get_object_or_404(taks, pk=task_id, User=request.user)
    if request.method=="POST":
        tarea.Datecompleted=timezone.now()
        tarea.save()
        return redirect('Taks')
        
@login_required(login_url='/Autenticacion/login')   
def deletetask(request,task_id):
    tarea = get_object_or_404(taks, User=request.user,pk=task_id)
    if request.method=="POST":
        tarea.delete()
        return redirect('Taks')

@login_required(login_url='/Autenticacion/login')
def taskcompleted(request):
    tasks = taks.objects.filter(User=request.user, Datecompleted__isnull=False ).order_by('-Datecompleted')
    return render(request,'Complete.html',{'task':tasks})