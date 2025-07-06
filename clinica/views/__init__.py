from .consultas import consulta_create
from .pacientes import paciente_create
from .medicos import medico_create
from .prescricao import prescricao_create
from .registro import registro_create

# Se você tiver a view home no arquivo home.py, importe também:

from clinica.api_views import PacienteViewSet, MedicoViewSet, ConsultaViewSet, RegistroSaudeViewSet, PrescricaoViewSet

from django.shortcuts import render

def home(request):
    return render(request, 'base.html')
