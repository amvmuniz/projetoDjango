from django.shortcuts import render, redirect
from .models import Produto
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages



# Cadastrar Produto
def cadastrar_produto(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        nome = request.POST.get('nome')

        Produto.objects.create(
            descricao=descricao,
            preco=preco,
            nome=nome,
        )

        return redirect('/lista')

    return render(request, 'cadastro.html')

# Listar Produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista.html', {'produtos': produtos})
def cadastrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'cadastrouser.html', {'erro': 'Usuário já existe.'})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('/cadastro/')  # Ou qualquer rota protegida

    return render(request, 'cadastrouser.html')