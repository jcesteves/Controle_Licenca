from django.db import models
from django.urls import reverse


class Estoque(models.Model):
    produto = models.CharField('Produto', max_length=150, unique=True)
    fornecedor = models.CharField('Fornecedor', max_length=100)
    contrato = models.CharField('Contrato', max_length=20)
    aquisicoes = models.IntegerField('Aquisições')
    quantidade_disponivel = models.IntegerField('Quantidade Disponível')
    reservadas = models.IntegerField('Reservadas')
    estoque = models.IntegerField('Estoque', blank=True, null=True)
    data = models.DateTimeField('Data Cadastro', auto_now_add=True)
    dt = models.DateField('Data', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('listar_estoque')

    @property
    def total_estoque(self):
        self.estoque = self.quantidade_disponivel + self.reservadas
        Estoque.save(self)
        return self.estoque

    def __str__(self):
        return str(self.produto) + str(self.fornecedor) + str(self.contrato) + \
               str(self.aquisicoes) + str(self.quantidade_disponivel) \
               + str(self.reservadas) + str(self.estoque) + str(self.data) + str(self.dt)
