from django.contrib import admin
from .models import Estoque


admin.site.site_header = 'Administração - Sistema de Controle de Licença'
admin.site.site_title = 'Admin- Licença'
admin.site.index_title = ''

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'aquisicoes', 'quantidade_disponivel', 'reservadas', 'estoque')
    







