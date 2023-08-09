from django import forms
from .models import Automovel, MarcaAutomovel, ModeloAutomovel
from django.forms.widgets import ClearableFileInput

class AutomovelForm(forms.ModelForm):
    ano = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1900}))

    class Meta:
         model = Automovel
         fields = ['placa_automovel', 'cor', 'nro_portas', 'marca', 'tipo_combustivel', 'tipo_combustivel', 'quilometragem','renavam', 'valor_locacao', 'modelo', 'ano', 'categoria', 'status','chassi', 'imagem']
         widgets = {
            'imagem': forms.ClearableFileInput(),
            }

    def __init__(self, *args, **kwargs):
        # Define uma class CSS 'form-control' e o adiciona um js pra deixar as letras em maiúsculas.
        for l in self.base_fields:
            self.base_fields[l].widget.attrs['class'] = 'form-control'
            self.base_fields[l].widget.attrs['onkeyup'] = 'this.value=this.value.toUpperCase()'
        super(AutomovelForm, self).__init__(*args, **kwargs)
        
class MarcaAutomovelForm(forms.ModelForm):
    class Meta:
        model = MarcaAutomovel
        fields = ['nome']
        
class ModeloAutomovelForm(forms.ModelForm):
    class Meta:
        model = ModeloAutomovel
        fields = ['marca', 'nome']