from django.db import models
from django.contrib.auth.models import User

class taks(models.Model):
    Title= models.CharField(max_length=150)
    Description = models.TextField(blank=True)
    Created= models.DateTimeField(auto_now_add=True)
    Datecompleted= models.DateTimeField(null=True, blank=True)
    important= models.BooleanField(default=False)
    User= models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name="Task"
        verbose_name_plural="Tasks"
        db_table="Tasks"
    def __str__(self):
        return "La tarea {} pertenece a {}".format(self.Title,self.User)
# Create your models here.
