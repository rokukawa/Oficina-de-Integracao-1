import fornecedor
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from fornecedor.forms import *
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def cadastro_fornecedor(request):
    fornecedor_form = FornecedorForms(request.POST or None)
    contexto = {'fornecedor_form': fornecedor_form}

    if request.method == 'POST':
        if fornecedor_form.is_valid():
            fornecedor_form.save()
            return redirect('lista_fornecedores')  
        else:
            return render(request, 'cadastrar/cadastro_fornecedor.html', contexto)
    else:
        return render(request, 'cadastrar/cadastro_fornecedor.html', contexto)


def lista_fornecedores(request):
    lista_fornecedores = Fornecedor.objects.all()
    contexto = {'lista_fornecedores': lista_fornecedores}
    return render(request, 'listar/lista_fornecedores.html', contexto)


def exclui_fornecedor(request, fornecedor_id):
    fornecedor = Fornecedor.objects.filter(pk=fornecedor_id)
    fornecedor.delete()
    return redirect('dashboard')


def edita_fornecedor(request, fornecedor_id):
    edita_fornecedor = Fornecedor.objects.filter(pk=fornecedor_id)
    contexto = {'edita_fornecedor': edita_fornecedor}
    return render(request, 'editar/edita_fornecedor.html', contexto)


def atualiza_fornecedor(request):
    if request.method == 'POST':
        fornecedor_id = request.POST['fornecedor_id']
        f = Fornecedor.objects.get(pk=fornecedor_id)
        f.nome_fornecedor = request.POST['nome_fornecedor']
        f.cnpj = request.POST['cnpj']
        f.celular = request.POST['celular']
        f.residencial = request.POST['residencial']
        f.comercial = request.POST['comercial']
        f.rua = request.POST['rua']
        f.bairro = request.POST['bairro']
        f.cidade = request.POST['cidade']
        f.cep = request.POST['cep']
        f.numero = request.POST['numero']
        f.complemento = request.POST['complemento']
        f.save()
        return redirect('lista_fornecedores') 