from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=200, help_text='Nome do Funcionario')
    
    def __str__(self):
        return self.nome
