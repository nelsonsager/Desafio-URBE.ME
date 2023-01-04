from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

#("armazenar no bd", "aparecer pro usuario")
LISTA_CATEGORIAS = (
    ("COMERCIAL", "Comercial"),
    ("RESIDENCIAL", "Residencial"),
    ("OUTROS", "Outros"),
)

# criar o incorporador
class Incorporador(models.Model):
    titulo = models.CharField(max_length=100) 
    thumb = models.ImageField(upload_to='thumb_incorporadores')
    descricao = models.TextField(max_length=2000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
  
class Usuario(AbstractUser):
    incorporadoras_vistas = models.ManyToManyField("Incorporador")

# criar os investimentos 
