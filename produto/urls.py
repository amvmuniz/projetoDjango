from django.urls import path
from . import views
from .views import cadastrar_usuario

urlpatterns = [
    path('cadastro/', views.cadastrar_produto, name='cadastrar_produto'),
    path('lista/', views.lista_produtos, name='lista_produtos'),
    path('cadastro_usuario/', cadastrar_usuario, name='cadastro_usuario'),
    # outras rotas como cadastro de produto e lista
]
