from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario

@login_required
def home(request):
    usuario = request.user
    return render(request, 'core/index.html', locals())
