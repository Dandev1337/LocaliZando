from django.urls import path
from . import views
app_name= 'automoveis'

urlpatterns = [
    # Listar todos os automóveis
    path('gerencia/', views.automovel_crud, name='automovel_crud'),
    path('list', views.automovel_list, name='automovel_list'),
    path('automoveis/<int:automovel_id>/', views.automovel_detail, name='automovel_detail'),
    path('automoveis/adicionar/', views.automovel_create, name='automovel_create'),
    path('automoveis/<int:automovel_id>/atualizar/', views.automovel_update, name='automovel_update'),
    path('automoveis/<int:automovel_id>/excluir/confirmar/', views.automovel_confirm_delete, name='automovel_confirm_delete'),
    path('automoveis/<int:automovel_id>/atualizar/sucesso/', views.sucesso, name='sucesso'),
    
# URLs para MarcaAutomovel
    path('marca/create/', views.marca_create, name='marca_create'),
    path('marca/<int:marca_id>/', views.marca_detail, name='marca_detail'),
    path('marca/<int:marca_id>/update/', views.marca_update, name='marca_update'),
    path('marca/<int:marca_id>/delete/', views.marca_delete, name='marca_delete'),
    path('marca/gerencia/', views.marca_list, name='marca_list'),
    

    # URLs para ModeloAutomovel
    path('modelo/<int:modelo_id>/', views.modelo_detail, name='modelo_detail'),
    path('modelo/create/', views.modelo_create, name='modelo_create'),
    path('modelo/<int:modelo_id>/update/', views.modelo_update, name='modelo_update'),
    path('modelo/gerencia/', views.modelo_list, name='modelo_list'),
    path('modelo/<int:modelo_id>/delete/', views.modelo_delete, name='modelo_delete'),
    
]