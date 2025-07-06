from django.db import models
from .validators import validador_email, validador_telefone, validador_crm

# ===== CONSTANTES =====
NIVEIS_ATIVIDADE = [
    ('leve', 'Leve'),
    ('moderada', 'Moderada'),
    ('intensa', 'Intensa'),
]

NIVEIS_PRESSAO = [
    ('baixa', 'Baixa'),
    ('normal', 'Normal'),
    ('alta', 'Alta'),
    ('muito alta', 'Muito Alta'),
]

ESPECIALIDADES_MEDICAS = [
    ('cardiologista', 'Cardiologista'),
    ('dentista', 'Dentista'),
    ('geriatra', 'Geriatra'),
    ('ginecologista', 'Ginecologista'),
    ('neurologista', 'Neurologista'),
    ('ortopedista', 'Ortopedista'),
    ('pediatra', 'Pediatra'),
]

# ===== MODELOS =====

# Paciente
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(validators=[validador_email])
    telefone = models.CharField(max_length=20, validators=[validador_telefone])

    def __str__(self):
        return self.nome

# Médico
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(
        max_length=100,
        choices=ESPECIALIDADES_MEDICAS,
        default='cardiologista'
    )
    crm = models.CharField(
        max_length=6,
        unique=True,
        validators=[validador_crm]
    )
    telefone = models.CharField(
        max_length=20,
        validators=[validador_telefone]
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        validators=[validador_email]
    )

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"

# Registro de Saúde
class RegistroSaude(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='registros')
    telefone = models.CharField(max_length=20, validators=[validador_telefone])
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    pressao_arterial = models.CharField(max_length=20, choices=NIVEIS_PRESSAO, default='normal')
    nivel_atividade = models.CharField(max_length=20, choices=NIVEIS_ATIVIDADE, default='leve')
    data_avaliacao = models.DateField()
    data_retorno = models.DateField()

    def __str__(self):
        return f"{self.paciente.nome} - {self.data_avaliacao}"

# Consulta
class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    motivo = models.TextField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente.nome} com {self.medico.nome} em {self.data.strftime('%d/%m/%Y %H:%M')}"

# Prescrição
class Prescricao(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescrição - {self.consulta.paciente.nome} ({self.data})"