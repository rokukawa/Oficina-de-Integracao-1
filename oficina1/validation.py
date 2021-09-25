from fornecedor.models import Fornecedor
from caneta.models import Caneta


def campo_contem_numero(valor_campo, nome_campo, lista_de_erros):   
    nome_do_campo = nome_campo.replace('_', ' ') 

    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = f'Campo {nome_do_campo} não pode conter números.'

def campo_contem_letra(valor_campo, nome_campo, lista_de_erros):
    nome_do_campo = nome_campo.replace('_', ' ') 
    
    if any(char.isalpha() for char in valor_campo):
        lista_de_erros[nome_campo] = f'Campo {nome_do_campo} não pode conter letras.'

def campo_contem_simbolos(valor_campo, nome_campo, lista_de_erros):
    nome_do_campo = nome_campo.replace('_', ' ')
    simbolos_invalidos = "!@#$%^&*()_-+={}[]"

    for char in valor_campo:
        if char in simbolos_invalidos:
            lista_de_erros[nome_campo] = f'Campo {nome_do_campo} não pode conter símbolos.'
            break

def cadastro_existente(nome_campo, campo_valor, lista_de_erros):
    fornecedor = Fornecedor.objects.filter(cnpj=campo_valor).exists()

    if nome_campo == 'codigo':
        nome_auxiliar = 'Código do relatório'
    else:
        nome_auxiliar = nome_campo.capitalize()

    if fornecedor is not None:
        lista_de_erros[nome_campo] = f'{nome_auxiliar} já existe.'

def caneta_existente(nome_campo, campo_modelo, campo_cor, campo_ponta, lista_de_erros):
    caneta = Caneta.objects.filter(modelo=campo_modelo).filter(cor=campo_cor).filter(ponta=campo_ponta)

    if caneta.count() != 0:
        lista_de_erros[nome_campo] = f'Caneta já existe.'

def remove_espaço(valor_campo):
    valor_campo = valor_campo.strip()