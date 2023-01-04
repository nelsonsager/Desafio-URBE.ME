from django.contrib import admin
from .models import Incorporador, Usuario #arquivo modelo que esta na mesma pasta 
from django.contrib.auth.admin import UserAdmin

# só existe porque queremos que no admin apareca um campo personalizado visualizacoes
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico",{'fields': ('incorporadoras_vistas',)}),
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Incorporador)
admin.site.register(Usuario, UserAdmin)