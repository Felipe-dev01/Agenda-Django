from django.contrib import admin
from core.models import Evento

# Register your models here.

# Classe para melhor visualização no django admin
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento')


admin.site.register(Evento, EventoAdmin)