from .views import (
    IndexTemplateView, 
    FuncionarioListView, 
    FuncionarioUpdateView, 
    FuncionarioCreateView,
    FuncionarioDeleteView,
)
from django.urls import path


app_name = 'website'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name="cadastra_funcionario"),
    path('funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),
]