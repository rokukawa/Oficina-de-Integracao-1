from usuario.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/caneta', views.cadastro_caneta, name='cadastro_caneta'),
    path('cadastro/lote', views.cadastro_lote, name='cadastro_lote'),
    path('lista/canetas', views.lista_canetas, name='lista_canetas'),
    path('lista/lote', views.lista_lote, name='lista_lote'),
    path('relatorio', views.gerar_relatorio, name='relatorio'),
    path('lista/relatorio', views.listar_relatorio, name='lista_relatorio'),
    path('exclui/caneta/<int:caneta_id>', views.exclui_caneta, name='exclui_caneta'),
    path('exclui/lote/<int:lote_id>', views.exclui_lote, name='exclui_lote'),
    path('exclui/relatorio/<int:relatorio_id>', views.exclui_relatorio, name='exclui_relatorio'),
    path('edita/caneta/<int:caneta_id>', views.edita_caneta, name='edita_caneta'),
    path('atualiza/caneta', views.atualiza_caneta, name='atualiza_caneta'),
    path('edita/lote/<int:lote_id>', views.edita_lote, name='edita_lote'),
    path('atualiza/lote', views.atualiza_lote, name='atualiza_lote'),
    path('edita/relatorio/<int:relatorio_id>', views.edita_relatorio, name='edita_relatorio'),
    path('atualiza/relatorio', views.atualiza_relatorio, name='atualiza_relatorio')
]