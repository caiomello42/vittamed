import re
from django.core.validators import RegexValidator

validador_telefone = RegexValidator(
    regex=r'^\(\d{2}\)\s\d{4,5}-\d{4}$',
    message='O telefone deve estar no formato (XX) XXXXX-XXXX'
)

validador_crm = RegexValidator(
    regex=r'^\d{6}$',
    message='O CRM deve conter exatamente 6 dígitos numéricos.'
)

validador_email = RegexValidator(
    regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    message='O e-mail deve estar no formato válido.'
)