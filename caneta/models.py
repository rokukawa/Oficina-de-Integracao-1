from django.db import models
from django.db.models.deletion import CASCADE
from fornecedor.models import Fornecedor
from datetime import datetime

# Create your models here.

class Caneta(models.Model):
    modelo = models.CharField(max_length=45, null=False, blank=True)
    cor = models.CharField(max_length=45, null=False, blank=True)
    ponta = models.CharField(max_length=45, null=False, blank=True)
    
    def __str__(self):
        return self.modelo

class Lote(models.Model):
    codigo_maquina = models.CharField(max_length=45, null=False, blank=True)
    data_fabricação = models.DateField(null=False)
    quantidade = models.IntegerField(null=False)
    caneta = models.ForeignKey(Caneta, on_delete=CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=CASCADE)

    def __str__(self):
        return self.codigo_maquina

class Relatorio(models.Model):
    lote = models.ForeignKey(Lote, on_delete=CASCADE)
    quantidade_falhas = models.IntegerField(null=False)
    codigo = models.CharField(max_length=45)

    