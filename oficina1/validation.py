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