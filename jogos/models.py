from django.db import models
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Jogo(models.Model):
    nome = models.CharField(max_length=200)


class JogoCategoria(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)