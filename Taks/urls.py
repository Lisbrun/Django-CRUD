
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Home, name='Principal'),
    path('Taks/', tasks, name='Taks'),
    path('createTask/', createTask, name='createTask'),
    path('Taks/<int:task_id>/', task_detail, name='Task_detail'),
    path('Taks/<int:task_id>/complete', completetask, name='complete_task'),
    path('Taks/<int:task_id>/Eliminar', deletetask, name='deletetask'),
    path('CompleteTask/', taskcompleted, name ="CompleteTask"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)