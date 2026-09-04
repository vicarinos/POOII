from django.db import models


class tarefa(models.Model):
    titulo = models.CharField(max_length= 100, null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, null= False, blank=False)
    prazoLimite = models.DateTimeField(null = False, blank=False)
    terminado_em = models.DateTimeField(null=True)


# Create your models here.
