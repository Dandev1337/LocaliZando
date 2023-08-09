from django.shortcuts import render, redirect
from .forms import ClienteForm, CargoForm, FuncionarioForm
from .models import Cliente, Cargo, Funcionario


def clientes(request):
    data = {}
    data['clientes'] = Cliente.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('cliente:url_cliente')
    else:
        data['form'] = ClienteForm()
        #form = ClienteForm()
    return render(request, 'clientes.html', data)

def funcionarios(request):
    data = {}
    data['funcionarios'] = Funcionario.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('cliente:url_funcionario')
    else:
        data['form'] = FuncionarioForm()
    return render(request, 'funcionarios.html', data)

def cargos(request):
    data = {}
    data['cargos'] = Cargo.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('cliente:url_cargo')
    else:
        data['form'] = CargoForm()
    return render(request, 'cargos.html', data)

def atualiza_cliente(request, pk):
    data = {}
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente) #Passar o formulario preenchido

    # Verificar se o form é valido
    if form.is_valid():
        form.save()  # Salva
        return redirect('cliente:url_cliente')  # E redireciona para a listagem

    data['form'] = form
    data['clientes'] = cliente # Enviando a transação pela URL, para ser possivel remover

    return render(request, 'atualizacliente.html', data)


def atualiza_funcionario(request, pk):
    data = {}
    funcionario = Funcionario.objects.get(pk=pk)
    form = FuncionarioForm(request.POST or None, instance=funcionario) #Passar o formulario preenchido

    # Verificar se o form é valido
    if form.is_valid():
        form.save()  # Salva
        return redirect('cliente:url_funcionario')  # E redireciona para a listagem

    data['form'] = form

    return render(request, 'atualizafuncionario.html', data)


def atualiza_cargo(request, pk):
    data = {}
    cargo = Cargo.objects.get(pk=pk)
    form = CargoForm(request.POST or None, instance=cargo)

    if form.is_valid():
        form.save()
        return redirect('cliente:url_cargo')

    data['form'] = form

    return render(request, 'atualizacargo.html', data)

def remover_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('cliente:url_cliente')

def remover_cargo(request, pk):
    cargo = Cargo.objects.get(pk=pk)
    cargo.delete()
    return redirect('cliente:url_cargo')

def remover_funcionario(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)
    funcionario.delete()
    return redirect('cliente:url_funcionario')
