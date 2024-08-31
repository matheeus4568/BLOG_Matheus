from django.db import models

# Create your models here.


class Hobbie(models.Model):
    nome = models.CharField(max_length=100)
    image = models.ImageField()
    data_inicio = models.DateField()
    nota = models.IntegerField()
    sobre = models.CharField(max_length=300)
    
    def __str__ (self):
        return self.nome
    
class Namorado(models.Model):
    nome = models.CharField(max_length=200)
    image = models.ImageField()
    idade = models.IntegerField()
    voltaria_a_namorar = models.BooleanField(default=False)
    ele_traiu = models.BooleanField(default=True)
    eu_trai = models.BooleanField(default=False)
    nota = models.IntegerField()
    sobre = models.CharField(max_length=300)
    
    def __str__ (self):
        return self.nome
    
class MaisFotos(models.Model):
    titulo = models.CharField(max_length=200)
    image = models.ImageField()
    
    def __str__(self):
        return self.titulo