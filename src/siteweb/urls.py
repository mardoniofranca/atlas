from django.urls import path
from . import views


urlpatterns = [
        path("", views.index, name="index"),
        path("login/", views.login, name="login"),
        path("menu/", views.menu, name="menu"),
        path("menu_cadastro/", views.menu_cadastro, name="menu_cadastro"),


        path("cliente/", views.cliente, name="cliente"),
        path('cliente/cadastrar/', views.cliente_cadastrar, name='cliente_cadastrar'),
        path('cliente/<int:id>/', views.cliente_detalhe, name='cliente_detalhe'),
        path('cliente/<int:id>/editar/', views.cliente_editar, name='cliente_editar'),
        path('cliente/<int:id>/excluir/', views.cliente_excluir, name='cliente_excluir'),
]