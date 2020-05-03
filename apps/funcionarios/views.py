from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        # Filtra o funcionario por empresa
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada) 

class FuncionariosEdit(UpdateView):
    model  = Funcionario
    fields = ['nome', 'departamento']

class FuncionariosDelete(DeleteView):
    model       = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionariosCreate(CreateView):
    model  = Funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()

        return super(FuncionariosCreate, self).form_valid(form)