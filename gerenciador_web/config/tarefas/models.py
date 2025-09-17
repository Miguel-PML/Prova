from django.db import models

# Create your models here.

class tarefa(models.Model):

    titulo = models.CharField(max_length = 200)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add = True)
    concluido = models.BooleanField(default=False)

#Exibir titulo padrão
def __str__(self):
    return self.titulo