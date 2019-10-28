from django.urls import path
from .views import List_estoque, Edit_estoque, Create_estoque, Delete_estoque, index, utilizou_licenca, ExportarExcel

urlpatterns = [
    path('', index, name='index'),
    path('estoque/', List_estoque.as_view(), name='listar_estoque'),
    path('editar/<int:pk>', Edit_estoque.as_view(), name='editar_estoque'),
    path('cadastrar/', Create_estoque.as_view(), name='cadastrar_estoque'),
    path('excluir/<int:pk>/', Delete_estoque.as_view(), name='excluir_estoque'),
    path('exportar-excel/', ExportarExcel.as_view(), name='exportar_excel'),
    path('utilizou_licenca/<int:pk>/', utilizou_licenca.as_view(), name='utilizou_licenca'),
 ]