from django.shortcuts import render
from .models import Hobbie, Namorado, MaisFotos

# Create your views here.

def index(request):
    maisfotos = MaisFotos.objects.all()
    contexto = {
        'maisfotos': maisfotos,
    }
    return render(request, 'matheus/index.html', contexto)

def hobbies(request):
    hobbies = Hobbie.objects.all()
    contexto = {
        'hobbies': hobbies,
    }
    return render(request, 'matheus/hobbies.html', contexto)

def namorados(request):
    namorados = Namorado.objects.all()
    contexto = {
        'namorados': namorados,
    }
    return render(request, 'matheus/namorados.html', contexto)

def sobre(request):
    return render(request, 'matheus/sobre.html')