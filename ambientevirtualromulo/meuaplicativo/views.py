from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    return render (request, 'meuaplicativo/index.html')

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'apelido', 'cpf', 'idade', 'email', 'telefone']


def cadastrar_cliente(request, template_name='meuaplicativo/cliente_form.html'):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        #return redirect('listar_produto')
    return render(request, template_name, {'form': form})
