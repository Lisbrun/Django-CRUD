from django.forms import ModelForm
from .models import taks
class formTask(ModelForm):
    class Meta:
        model = taks
        fields = ['Title','Description','important']