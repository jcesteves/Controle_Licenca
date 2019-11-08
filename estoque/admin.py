from django.contrib import admin
from .models import Estoque


admin.site.site_header = 'Administração - Sistema de Controle de Licença'
admin.site.site_title = 'Admin- Licença'
admin.site.index_title = ''

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    fields = ('produto', 'fornecedor', 'contrato', 'aquisicoes', 'quantidade_disponivel', 'reservadas', 'estoque', 'data')
    list_display = ('produto', 'fornecedor', 'contrato', 'aquisicoes', 'quantidade_disponivel', 'reservadas', 'estoque', 'data')
    search_fields = ('produto', 'fornecedor', 'contrato', 'aquisicoes', 'quantidade_disponivel', 'reservadas', 'estoque', 'data')
    list_filter = ('produto', 'fornecedor', 'contrato', 'aquisicoes', 'quantidade_disponivel', 'reservadas', 'estoque', 'data')
    readonly_fields = ('data',)
    







