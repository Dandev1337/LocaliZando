from django.shortcuts import render, redirect
from locacao.forms import *
from locacao.models import Locacao


def locacoes(request):
    data = {}
    data['locacoes'] = Locacao.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('locacao:url_locacao')
    else:
        data['form'] = LocacaoForm()
        # form = ClienteForm()
    return render(request, 'locacoes.html', data)

def atualiza_locacao(request, pk):
    data = {}
    locacao = Locacao.objects.get(pk=pk)
    form = LocacaoForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        return redirect('locacao:url_locacao')

    data['form'] = form

    return render(request, 'atualizalocacao.html', data)

def remover_locacao(request, pk):
    locacao = Locacao.objects.get(pk=pk)
    locacao.delete()
    return redirect('locacao:url_locacao')
