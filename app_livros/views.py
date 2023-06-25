from django.shortcuts import render


def home(request):
    return render(request, "app_livros/pages/home.html")


def add_movimentacao(request):
    return render(request, "app_livros/pages/add_movimentacao.html")
