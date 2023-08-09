from django.urls import path
from cliente.views import funcionarios, cargos, clientes
from cliente.views import remover_cliente, remover_cargo, remover_funcionario
from cliente.views import atualiza_cliente, atualiza_funcionario, atualiza_cargo


app_name = 'cliente'

urlpatterns = [
    path('funcionarios/', funcionarios, name='url_funcionario'),
    path('cargos/', cargos, name='url_cargo'),
    path('clientes/', clientes, name='url_cliente'),
    path('atualizacliente/<int:pk>/', atualiza_cliente, name='url_atualizacliente'),
    path('atualizafuncionario/<int:pk>/', atualiza_funcionario, name='url_atualizafuncionario'),
    path('atualizacargo/<int:pk>/', atualiza_cargo, name='url_atualizacargo'),
    path('remover_cliente/<int:pk>/', remover_cliente, name='url_removercliente'),
    path('remover_cargo/<int:pk>/', remover_cargo, name='url_removercargo'),
    path('remover_funcionario/<int:pk>/', remover_funcionario, name='url_removerfuncionario'),
]
