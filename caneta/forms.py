from fornecedor.views import lista_fornecedores
from django import forms
from django.db.models import fields
from django.forms import widgets
from caneta.models import *
from oficina1.validation import *

class CanetaForms(forms.ModelForm):
    class Meta:
        model = Caneta
        fields = '__all__'
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o modelo da caneta'}),
            'cor': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a cor da caneta'}),
            'ponta': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a ponta da caneta'}),
        }

    def clean(self):
        lista_de_erros = {}
        modelo = self.cleaned_data.get('modelo')
        cor = self.cleaned_data.get('cor')
        ponta = self.cleaned_data.get('ponta')

        campo_contem_numero(cor, 'cor', lista_de_erros)
        campo_contem_simbolos(cor, 'cor', lista_de_erros)
        campo_contem_simbolos(modelo, 'modelo', lista_de_erros)
        campo_contem_simbolos(ponta, 'ponta', lista_de_erros)

        caneta_existente('modelo', modelo, cor, ponta, lista_de_erros)

        remove_espaço(modelo)
        remove_espaço(cor)
        remove_espaço(ponta)
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data

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

    def clean(self):
        lista_de_erros = {}

        codigo_maquina = self.cleaned_data.get('codigo_maquina')

        campo_contem_simbolos(codigo_maquina, 'codigo_maquina', lista_de_erros)

        remove_espaço(codigo_maquina)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        
        return self.cleaned_data



class RelatorioForms(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = '__all__'
        widgets = {
            'lote': forms.Select(attrs={'class': 'item', 'max_length':100, 'placeholder':'Selecione o Lote da caneta'}),
            'quantidade_falhas': forms.NumberInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a quantidade de canetas falhas'}),
            'codigo': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o código do relatório'}),
        }

    def clean(self):
        lista_de_erros = {}

        codigo_relatorio = self.cleaned_data.get('codigo')

        campo_contem_simbolos(codigo_relatorio, 'codigo', lista_de_erros)
        
        cadastro_existente('codigo', codigo_relatorio, lista_de_erros)

        remove_espaço(codigo_relatorio)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        
        return self.cleaned_data
        