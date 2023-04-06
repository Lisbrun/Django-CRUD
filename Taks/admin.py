from django.contrib import admin
from .models import taks
class taskAdmin(admin.ModelAdmin):
    readonly_fields=('Created',)
admin.site.register(taks, taskAdmin)
# Register your models here.
