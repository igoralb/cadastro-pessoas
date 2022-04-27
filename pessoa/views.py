from django.shortcuts import render
from django.views.generic import ListView, CreateView
#^^classe do django propia para fornecer uma tela para a listagem de pessoas
from .models import Pessoa
from .forms import PessoaForm

#model diz o dado q ela vai trabalhar e o queryset é o
#filtro para saber o que sera pesquisado no banco
class ListaPessoaView(ListView):
	model = Pessoa 
	queryset = Pessoa.objects.all().order_by('nome_completo')

class PessoaCreateView(CreateView):
	model = Pessoa
	form_class = PessoaForm
	sucess_url = '/pessoa/'