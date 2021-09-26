from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Categoria
from .serializers import CategoriaSerializer


# Create your views here.

def index(request):
    return HttpResponse("Bem vindo ao MMO Box")


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer