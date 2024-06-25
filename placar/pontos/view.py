from django.shortcuts import render, get_object_or_404, redirect
from .model import Ponto

def index(request):
    pontos_joao = Ponto.objects.filter(origem='joao')
    pontos_benja = Ponto.objects.filter(origem='benja')
    total_joao = pontos_joao.count()
    total_benja = pontos_benja.count()
    return render(request, 'pontos/index.html', {
        'pontos_joao': pontos_joao,
        'pontos_benja': pontos_benja,
        'total_joao': total_joao,
        'total_benja': total_benja
    })
