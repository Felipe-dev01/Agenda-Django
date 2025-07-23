from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null = True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação')
    # O parâmetro após user diz que se o user for deletado os eventos tambem são!!!
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    # Método para melhor visualização no django admin
    def __str__(self):
        return self.titulo
    
    def get_data_criacao(self):
        return self.data_evento.strftime('%d/%m/%Y, %H:%M Hrs.')
    
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
    
    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False