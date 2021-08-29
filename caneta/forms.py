from django import forms
from django.db.models import fields
from django.forms import widgets
from caneta.models import *

class CanetaForms(forms.ModelForm):
    class Meta:
        model = Caneta
        fields = '__all__'
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o modelo da caneta'}),
            'cor': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a cor da caneta'}),
            'ponta': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a ponta da caneta'}),
        }


class LoteForms(forms.ModelForm):
    class Meta:
        model = Lote
        fields = '__all__'
        widgets = {
            'codigo_maquina': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o código de fabricação da máquina da caneta'}),
            'data_fabricação': forms.DateInput(attrs={'class': 'item', 'max_length':100, 'type':'date', 'placeholder':'Informe a data de fabricação da caneta'}),
            'quantidade': forms.NumberInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a quantidade de caneta'}),
            'caneta': forms.Select(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o tipo de caneta'}),
            'fornecedor': forms.Select(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o fornecedor de caneta'}),
        }


class RelatorioForms(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = '__all__'
        widgets = {
            'lote': forms.Select(attrs={'class': 'item', 'max_length':100, 'placeholder':'Selecione o Lote da caneta'}),
            'quantidade_falhas': forms.NumberInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a quantidade de canetas falhas'}),
            'codigo': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o código do relatório'}),
        }
        