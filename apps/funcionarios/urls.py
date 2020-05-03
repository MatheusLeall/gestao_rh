from django.urls import path
from .views import FuncionariosList, FuncionariosEdit, FuncionariosDelete, FuncionariosCreate

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionariosCreate.as_view(), name='create_funcionario'),
    path('alterar/<int:pk>', FuncionariosEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>', FuncionariosDelete.as_view(), name='delete_funcionario'),
]