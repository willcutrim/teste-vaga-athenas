from . import views
from django.urls import path

urlpatterns = [
    path('incluir/', views.incluir),
    path('', views.index),
    path('listar_pessoas/', views.listar_pessoas),
    path('obter_pessoa/', views.obter_pessoa),
    path('excluir_pessoa/<int:pessoa_id>', views.excluir_pessoa),
    path('atualizar_pessoa/<str:pessoa_id>', views.atualizar_pessoa),
    path('calcular_peso_ideal/<int:pessoa_id>', views.calcular_peso_ideal),
]
 