from django.contrib import admin
from .models import Estoque


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'aquisicoes', 'quantidade_disponivel', 'reservadas', 'estoque')
    







