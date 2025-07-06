from django.shortcuts import render, redirect
from rest_framework import viewsets, generics, filters
from clinica.models import Paciente, Medico, Consulta, Prescricao, RegistroSaude

def consulta_create(request):
    if request.method == 'POST':
        # Pegando dados do formulário (ajuste os nomes conforme seu HTML)
        medico_id = request.POST.get('medico_select')
        paciente_id = request.POST.get('consulta_paciente_select')
        data_hora = request.POST.get('data_hora_consulta')
        motivo = request.POST.get('motivo')
        observacoes = request.POST.get('observacoes')

        # Validação simples (você pode melhorar)
        errors = {}
        if not medico_id:
            errors['medico'] = 'Médico é obrigatório.'
        if not paciente_id:
            errors['paciente'] = 'Paciente é obrigatório.'
        if not data_hora:
            errors['data_hora'] = 'Data e hora são obrigatórios.'
        if not motivo:
            errors['motivo'] = 'Motivo é obrigatório.'

        if errors:
            # Recarrega o formulário com mensagens de erro
            context = {
                'errors': errors,
                'medicos': Medico.objects.all(),
                'pacientes': Paciente.objects.all(),
                'form_data': request.POST,
            }
            return render(request, 'consulta/form.html', context)

        # Salva a consulta
        medico = Medico.objects.get(id=medico_id)
        paciente = Paciente.objects.get(id=paciente_id)
        consulta = Consulta.objects.create(
            medico=medico,
            paciente=paciente,
            data_hora_consulta=data_hora,
            motivo=motivo,
            observacoes=observacoes
        )

        # Redireciona para a página principal ou uma página de sucesso
        return redirect('home')

    # GET - exibe o formulário vazio
    context = {
        'medicos': Medico.objects.all(),
        'pacientes': Paciente.objects.all(),
    }
    return render(request, 'consulta/form.html', context)



def home(request):
    context = {
        'medicos': Medico.objects.all(),
        'pacientes': Paciente.objects.all(),
        # se tiver outros dados para os forms, inclua aqui
    }
    return render(request, 'base.html', context)

