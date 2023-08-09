from django.shortcuts import render, redirect, get_object_or_404
from .models import Automovel, MarcaAutomovel, ModeloAutomovel
from .forms import AutomovelForm, MarcaAutomovelForm, ModeloAutomovelForm

def automovel_list(request):
    automoveis = Automovel.objects.all()
    return render(request, 'automovel_list.html', {'automoveis': automoveis})

def automovel_detail(request, automovel_id):
    automovel = get_object_or_404(Automovel, id=automovel_id)
    return render(request, 'automovel_detail.html', {'automovel': automovel})

def automovel_create(request):
    if request.method == 'POST':
        form = AutomovelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'sucesso.html', {'mensagem': 'Automóvel salvo com sucesso!'})
    else:
        form = AutomovelForm()
    return render(request, 'automovel_form.html', {'form': form})

def sucesso(request, mensagem):
    return render(request, 'sucesso.html', {'mensagem': mensagem})

def automovel_update(request, automovel_id):
    automovel = get_object_or_404(Automovel, id=automovel_id)
    if request.method == 'POST':
        form = AutomovelForm(request.POST, instance=automovel)
        if form.is_valid():
            form.save()
            return render(request,'sucesso.html', {'mensagem': 'Automóvel salvo com sucesso!'})
    else:
        form = AutomovelForm(instance=automovel)
    return render(request, 'automovel_form.html', {'form': form})

def automovel_confirm_delete(request, automovel_id):
    automovel = get_object_or_404(Automovel, id=automovel_id)
    if request.method == 'POST':
        automovel.delete()
        return redirect('automovel_crud.html')
    return render(request, 'automovel_confirm_delete.html', {'automovel': automovel})
pass

def cardapio_veiculos(request):
    automoveis = Automovel.objects.all()
    return render(request, 'cardapio_veiculos.html', {'automoveis': automoveis})

def marca_list(request):
    marcas = MarcaAutomovel.objects.all()
    return render(request, 'marca_list.html', {'marcas': marcas})

def marca_detail(request, marca_id):
    marca = get_object_or_404(MarcaAutomovel, id=marca_id)
    return render(request, 'marca_detail.html', {'marca': marca})

def marca_create(request):
    if request.method == 'POST':
        form = MarcaAutomovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('automoveis:marca_list')
    else:
        form = MarcaAutomovelForm()
    return render(request, 'marca_form.html', {'form': form})

def marca_update(request, marca_id):
    marca = get_object_or_404(MarcaAutomovel, id=marca_id)
    if request.method == 'POST':
        form = MarcaAutomovelForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
    else:
        form = MarcaAutomovelForm(instance=marca)
    return render(request, 'marca_form.html', {'form': form})   

def marca_delete(request, marca_id):
    marca = get_object_or_404(MarcaAutomovel, id=marca_id)
    if request.method == 'POST':
        marca.delete()
        return redirect('automoveis:marca_list')
    return render(request, 'marca_confirm_delete.html', {'marca': marca})

def modelo_list(request):
    modelos = ModeloAutomovel.objects.all()
    return render(request, 'modelo_list.html', {'modelos': modelos})

def modelo_detail(request, modelo_id):
    modelo = get_object_or_404(ModeloAutomovel, id=modelo_id)
    return render(request, 'modelo_detail.html', {'modelo': modelo})


def modelo_create(request):
    if request.method == 'POST':
        form = ModeloAutomovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('automoveis:modelo_list')
    else:
        form = ModeloAutomovelForm()
    return render(request, 'modelo_form.html', {'form': form})


def modelo_update(request, modelo_id):
    modelo = get_object_or_404(ModeloAutomovel, id=modelo_id)
    if request.method == 'POST':
        form = ModeloAutomovelForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('modelo_list.html')
    else:
        form = ModeloAutomovelForm(instance=modelo)
    return render(request, 'modelo_form.html', {'form': form})


def modelo_delete(request, modelo_id):
    modelo = get_object_or_404(ModeloAutomovel, id=modelo_id)
    if request.method == 'POST':
        modelo.delete()
        return redirect('modelo_list.html')
    return render(request, 'modelo_confirm_delete.html', {'modelo': modelo})


def automovel_crud(request):
    if request.method == 'POST':
        form = AutomovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('automoveis:automovel_crud')
    else:
        form = AutomovelForm()

    automoveis = Automovel.objects.all()
    return render(request, 'automovel_crud.html', {'form': form, 'automoveis': automoveis})