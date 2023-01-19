from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    categorias = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=255, null=False, blank=False)
    categoria = models.CharField(max_length=255, choices=categorias, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=255, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"Fotografia [nome = {self.nome}]"