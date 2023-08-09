from django import forms
from locacao.models import Locacao
from cliente.models import Cliente, Funcionario
from automoveis.models import Automovel

class LocacaoForm(forms.ModelForm):

    data_locacao = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'date','class': 'form-control'}))
    data_devolucao = forms.DateField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))

    #status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices= Locacao.DEVOLUCAO_STATUS,
                               widget=forms.Select(attrs={'class': 'form-control'}))

    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(status='ATIVO'),
                                         widget=forms.Select(attrs={'class': 'form-control'}))

    veiculo = forms.ModelChoiceField(queryset=Automovel.objects.filter(status='Disponível'),
                                         widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Locacao
        fields = ('data_locacao','data_devolucao','status','funcionario','cliente', 'veiculo')
