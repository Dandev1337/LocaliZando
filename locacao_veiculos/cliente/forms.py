from django import forms
from cliente.models import Cliente, Funcionario, Cargo
class ClienteForm(forms.ModelForm):

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices = Cliente.STATUS, widget=forms.Select(attrs={'class': 'form-control'}))
    pontos_fidelidade = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput( attrs={'class':'form-control'}))

    class Meta:
        model = Cliente
        fields = ('nome','cpf','status','pontos_fidelidade', 'endereco', 'telefone', 'email')


class CargoForm(forms.ModelForm):

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    salario = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cargo
        fields = ('nome','descricao','salario')


class FuncionarioForm(forms.ModelForm):

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_admissao = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'date','class': 'form-control'}))
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput( attrs={'class':'form-control'}))

    class Meta:
        model = Funcionario
        fields = ('nome','cpf','data_admissao','cargo', 'endereco', 'telefone', 'email')