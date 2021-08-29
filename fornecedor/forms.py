from django import forms
from django.db.models import fields
from django.forms import widgets
from usuario.models import *

class FornecedorForms(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        widgets = {
            'nome_fornecedor': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o nome do forneceedor'}),
            'cnpj': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o CNPJ', 'data-mask':"00.000.000/0000-00"}),
            'celular': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o telefone celular', 'data-mask':"(00) 00000-0000"}),
            'comercial': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o telefone comercial', 'data-mask':"(00) 00000-0000"}),
            'residencial': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o telefone residencial', 'data-mask':"(00) 00000-0000"}),
            'rua': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o nome da rua'}),
            'numero': forms.TextInput(attrs={'class': 'item', 'max_length':45, 'placeholder':'Informe o número'}),
            'cidade': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a cidade'}),
            'cep': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o CEP', 'data-mask':"00000-000"}),
            'bairro': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o nome do bairro'}),
            'complemento': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o complemento'}),
        }