import json
import io
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Estoque
import xlwt


@login_required()
def index(request):
    return render(request, 'estoque/index.html')


class List_estoque(LoginRequiredMixin, ListView):
    model = Estoque


class Edit_estoque(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Estoque
    fields = ['produto', 'fornecedor', 'contrato', 'aquisicoes', 'quantidade_disponivel', 'reservadas']
    template_name_suffix = '_update_form'
    permission_required = 'estoque_Can_add_estoque'


class Create_estoque(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Estoque
    fields = ['produto', 'fornecedor', 'contrato', 'aquisicoes', 'quantidade_disponivel', 'reservadas']
    permission_required = ('estoque_Can__cadastrar')

    def get_success_url(self):
        return reverse('listar_estoque')


class Delete_estoque(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Estoque
    success_url = reverse_lazy('listar_estoque')
    permission_required = ('estoque_Can__deletar')

class utilizou_licenca(View):
    def post(self, *args, **kwargs):
        registro = Estoque.objects.get(id=kwargs['pk'])
        #json = serializers.serialize('json', registro)
        response = json.dumps({'estoque_atual': str(registro)})
        return HttpResponse(response, content_type='application/json')


#### View da extração do relatorio #####
class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="licença.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('licença')

        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns= ['produto', 'fornecedor', 'contrato', 'aquisicoes', 'quantidade_disponivel',
                  'reservadas', 'estoque']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()
        registros = Estoque.objects.all()
        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.produto, font_style)
            ws.write(row_num, 1, registro.fornecedor, font_style)
            ws.write(row_num, 2, registro.contrato, font_style)
            ws.write(row_num, 3, registro.aquisicoes, font_style)
            ws.write(row_num, 4, registro.quantidade_disponivel, font_style)
            ws.write(row_num, 5, registro.reservadas, font_style)
            ws.write(row_num, 6, registro.estoque, font_style)
            row_num += 1
        wb.save(response)
        return response
