from django.shortcuts import render, redirect
from clinica.models import Paciente, RegistroSaude

def registro_create(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente_select')
        telefone = request.POST.get('registro_telefone')
        peso = request.POST.get('peso')
        pressao = request.POST.get('pressao_arterial')
        atividade = request.POST.get('nivel_atividade')
        data_avaliacao = request.POST.get('data_avaliacao')
        data_retorno = request.POST.get('data_retorno')

        errors = {}
        if not paciente_id:
            errors['paciente'] = 'Paciente é obrigatório.'
        if not telefone:
            errors['telefone'] = 'Telefone é obrigatório.'
        # Continue as validações...

        if errors:
            context = {
                'errors': errors,
                'pacientes': Paciente.objects.all(),
                'form_data': request.POST,
            }
            return render(request, 'registro/form.html', context)

        paciente = Paciente.objects.get(id=paciente_id)
        registro = RegistroSaude.objects.create(
            paciente=paciente,
            telefone=telefone,
            peso=peso,
            pressao_arterial=pressao,
            nivel_atividade=atividade,
            data_avaliacao=data_avaliacao,
            data_retorno=data_retorno,
        )

        return redirect('home')

    context = {
        'pacientes': Paciente.objects.all(),
    }
    return render(request, 'registro/form.html', context)
