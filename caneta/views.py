from django.contrib import auth, messages
from django.shortcuts import render, redirect
from caneta.forms import *
from django.core.paginator import Paginator

# Create your views here.

def cadastro_caneta(request):
    caneta_form = CanetaForms(request.POST or None)
    contexto = {'caneta_form': caneta_form}

    if request.method == 'POST':
        if caneta_form.is_valid():
            caneta_form.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('lista_canetas')        
    else:
        return render(request, 'cadastrar/cadastro_caneta.html', contexto)


def cadastro_lote(request):
    lote_form = LoteForms(request.POST or None)
    contexto = {'lote_form': lote_form}

    if request.method == 'POST':
        if lote_form.is_valid():
            lote_form.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('lista_lote')
    else:
        return render(request, 'cadastrar/cadastro_lote.html', contexto)


def lista_canetas(request):
    lista_canetas = Caneta.objects.all()
    contexto = {'lista_canetas': lista_canetas}
    return render(request, 'listar/lista_canetas.html', contexto)


def lista_lote(request):
    lista_lote = Lote.objects.all()
    contexto = {'lista_lote': lista_lote}
    return render(request, 'listar/lista_lote.html', contexto)


def gerar_relatorio(request):
    relatorio_form = RelatorioForms(request.POST or None)
    contexto = {'relatorio_form': relatorio_form}
    
    if request.method == 'POST':
        if relatorio_form.is_valid():
            relatorio_form.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('lista_relatorio')
    else:
        return render(request, 'cadastrar/cadastro_relatorio.html', contexto)


def listar_relatorio(request):
    lista_relatorio = Relatorio.objects.all()
    contexto = {'lista_relatorio': lista_relatorio}
    return render(request, 'listar/lista_relatorio.html', contexto)

    
def exclui_caneta(request, caneta_id):
    caneta = Caneta.objects.filter(pk=caneta_id)
    caneta.delete()
    return redirect('dashboard')


def exclui_lote(request, lote_id):
    lote = Lote.objects.filter(pk=lote_id)
    lote.delete()
    return redirect('dashboard')


def exclui_relatorio(request, relatorio_id):
    relatorio = Relatorio.objects.filter(pk=relatorio_id)
    relatorio.delete()
    return redirect('dashboard')



def edita_caneta(request, caneta_id):
    edita_caneta = Caneta.objects.filter(pk=caneta_id)
    contexto = {'edita_caneta': edita_caneta}
    return render(request, 'editar/edita_caneta.html', contexto)


def atualiza_caneta(request):
    if request.method == 'POST':
        caneta_id = request.POST['caneta_id']
        c = Caneta.objects.get(pk=caneta_id)
        c.modelo = request.POST['modelo']
        c.cor = request.POST['cor']
        c.ponta = request.POST['ponta']
        c.save()
        return redirect('lista_canetas') 

        
def edita_lote(request, lote_id):
    edita_lote = Lote.objects.filter(pk=lote_id)
    contexto = {'edita_lote': edita_lote}
    return render(request, 'editar/edita_lote.html', contexto)


def atualiza_lote(request):
    if request.method == 'POST':
        lote_id = request.POST['lote_id']
        l = Lote.objects.get(pk=lote_id)
        l.codigo_maquina = request.POST['codigo_maquina']
        l.data_fabricação = request.POST['data_fabricação']
        l.quantidade = request.POST['quantidade']
        l.Caneta = request.POST['caneta']
        l.Fornecedor = request.POST['fornecedor']
        l.save()
        return redirect('lista_lote') 

        
def edita_relatorio(request, relatorio_id):
    edita_relatorio = Relatorio.objects.filter(pk=relatorio_id)
    contexto = {'edita_relatorio': edita_relatorio}
    return render(request, 'editar/edita_relatorio.html', contexto)


def atualiza_relatorio(request):
    if request.method == 'POST':
        relatorio_id = request.POST['relatorio_id']
        r = Relatorio.objects.get(pk=relatorio_id)
        r.Lote = request.POST['lote']
        r.quantidade_falhas = request.POST['quantidade_falhas']
        r.codigo = request.POST['codigo']
        r.save()
        return redirect('lista_relatorio') 