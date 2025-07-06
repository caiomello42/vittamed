# admin.py

from django.contrib import admin
from clinica.models import Paciente, Medico, Consulta, Prescricao, RegistroSaude

# Classe de customização opcional
class PacienteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'cpf']
    ordering = ['nome']

class MedicoAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'crm']
    ordering = ['nome']

# Registro com personalização
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico, MedicoAdmin)

# Registro dos demais modelos normalmente
admin.site.register(Consulta)
admin.site.register(Prescricao)
admin.site.register(RegistroSaude)
