from django.shortcuts import render,redirect
from .forms import FormularioContacto
from CRUD.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    if request.method == "POST":
        form = FormularioContacto(data=request.POST)
        if form.is_valid():
            Asunto = request.POST.get("Asunto")
            Nombre = request.POST.get("Nombre")
            Correo = request.POST.get("Correo")
            Contenido = request.POST.get("Contenido")
            Email = EmailMessage("{}".format(Asunto), "El usuario {} con el correo {} te ha enviado el siguiente mensaje: \n{}".format(
                Nombre, Correo, Contenido),"jmedinagu@unal.edu.co",[EMAIL_HOST_USER], reply_to=[EMAIL_HOST_USER])
            
            try:
                Email.send()
                return redirect("/Contacto/?valido")
            except:
                return redirect("/Contacto/?Error")
    
    form = FormularioContacto()
    return render(request, 'Contacto.html', {"form": form})
