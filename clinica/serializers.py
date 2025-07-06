from rest_framework import serializers
from .models import Paciente, Medico, Consulta, Prescricao, RegistroSaude

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta  # Corrigido para o modelo 'Consulta'
        fields = '__all__'

class PrescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescricao
        fields = '__all__'

class RegistroSaudeSerializer(serializers.ModelSerializer):        
    class Meta:
        model = RegistroSaude
        fields = '__all__'
