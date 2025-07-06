from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Paciente, Medico, Consulta, Prescricao, RegistroSaude
from .serializers import PacienteSerializer, MedicoSerializer, ConsultaSerializer, PrescricaoSerializer, RegistroSaudeSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    permission_classes = [IsAuthenticated]  
    ordering_fields = ['nome']
    

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para consultas
class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para prescrições
class PrescricaoViewSet(viewsets.ModelViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para registros de saúde
class RegistroSaudeViewSet(viewsets.ModelViewSet):
    queryset = RegistroSaude.objects.all()
    serializer_class = RegistroSaudeSerializer
    permission_classes = [IsAuthenticated]