from django import forms

class FormularioContacto(forms.Form):
    Asunto = forms.CharField(label="Nombre",required=True, max_length=25)
    Nombre= forms.CharField(label="Usuario",required=True, max_length=25)
    Correo = forms.EmailField(label="Correo",required=True,max_length=30)
    Contenido= forms.CharField(label="Contenido",max_length=300,widget=forms.Textarea)
    