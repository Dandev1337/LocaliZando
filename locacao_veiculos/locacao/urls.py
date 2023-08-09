from django.urls import path, include
# Importe as views do aplicativo "locacao"
from locacao.views import locacoes, atualiza_locacao, remover_locacao

app_name = 'locacao'

urlpatterns = [
   path('locacoes/', locacoes, name='url_locacao'),
   path('atualizalocacao/<int:pk>/', atualiza_locacao, name='url_atualizalocacao'),
   path('remover_locacao/<int:pk>/', remover_locacao, name='url_removerlocacao'),
]