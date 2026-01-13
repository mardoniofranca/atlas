from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormCliente
from .models import Cliente
from django.http import HttpResponse
from .models import Cliente_Hist
from django.core.paginator import Paginator

def index(request):
     return render(request, 'index.html')

def login(request):
     return render(request, 'index.html')

def menu(request):
    return render(request, "menu.html")

def menu_cadastro(request):
    return render(request, "menu_cadastro.html")

def cliente(request):
    qs = Cliente.objects.all().order_by('nome')

    filtros = {}
    nome = request.GET.get('nome')
    lideranca = request.GET.get('lideranca')
    fone = request.GET.get('fone')
    endereco = request.GET.get('endereco')
    email = request.GET.get('email')
    bairro = request.GET.get('bairro')
    zona = request.GET.get('zona')
    secao = request.GET.get('secao')

    if nome:
        qs = qs.filter(nome__icontains=nome)
        filtros['nome'] = nome

    if lideranca:
        qs = qs.filter(lideranca__icontains=lideranca)
        filtros['lideranca'] = lideranca

    if fone:
        qs = qs.filter(fone__icontains=fone)
        filtros['fone'] = fone

    if endereco:
        qs = qs.filter(endereco__icontains=endereco)
        filtros['endereco'] = endereco


    if email:
        qs = qs.filter(email__icontains=email)
        filtros['email'] = email

    if bairro:
        qs = qs.filter(bairro__icontains=bairro)
        filtros['bairro'] = bairro

  
    if zona:
        qs = qs.filter(zona__icontains=zona)
        filtros['zona'] = zona

    if secao:
        qs = qs.filter(secao__icontains=secao)
        filtros['secao'] = secao

    #  paginação
    paginator = Paginator(qs, 10)

    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)

    return render(request, 'cliente.html', {
        'page_obj': page_obj, 'filtros': filtros,
    })




def cliente_cadastrar(request):
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente')  # volta para a lista
    else:
        form = FormCliente()

    return render(request, 'cliente_form.html', {'form': form})

def cliente_detalhe(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'cliente_detalhe.html', {'cliente': cliente})

def cliente_editar(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        salvar_historico(cliente, 'ALTERACAO')
        
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():

            form.save()
            return redirect('cliente_detalhe', id=cliente.id)
    else:
        form = FormCliente(instance=cliente)

    return render(request, 'cliente_form.html', {'form': form})

def cliente_excluir(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        salvar_historico(cliente, 'EXCLUSAO')
        cliente.delete()
        return redirect('cliente')

    return render(request, 'cliente_confirmar_exclusao.html', {'cliente': cliente})



def salvar_historico(cliente, operacao):
    Cliente_Hist.objects.create(
        
        cliente_id_original = cliente.id,
        nome = cliente.nome,
        fone = cliente.fone,
        endereco = cliente.endereco,
        numero = cliente.numero,
        email = cliente.email,
        bairro = cliente.bairro,
        cidade = cliente.cidade,
        uf = cliente.uf,
        zona = cliente.zona,
        secao = cliente.secao,
        dia_aniv = cliente.dia_aniv,
        mes_aniv = cliente.mes_aniv,
        ano_aniv = cliente.ano_aniv,
        operacao = operacao
    )

def form(request):
    return render(request, "form.html")