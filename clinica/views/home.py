from .home import home
from django.shortcuts import render

def home(request):
    # Renderiza o template base.html como página inicial
    return render(request, 'base.html')
