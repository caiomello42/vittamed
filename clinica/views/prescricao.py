from django.shortcuts import render, redirect
from clinica.models import Prescricao, Consulta

def prescricao_create(request):
    if request.method == 'POST':
        consulta_id = request.POST.get('consulta_select')
        data_prescricao = request.POST.get('data_prescricao')
        descricao = request.POST.get('descricao')

        errors = {}
        if not consulta_id:
            errors['consulta'] = 'Consulta é obrigatória.'
        if not data_prescricao:
            errors['data_prescricao'] = 'Data da prescrição é obrigatória.'
        if not descricao:
            errors['descricao'] = 'Descrição é obrigatória.'

        if errors:
            context = {
                'errors': errors,
                'form_data': request.POST,
                'consultas': Consulta.objects.all(),
            }
            return render(request, 'prescricao/form.html', context)

        consulta = Consulta.objects.get(id=consulta_id)

        Prescricao.objects.create(
            consulta=consulta,
            data_prescricao=data_prescricao,
            descricao=descricao
        )
        return redirect('home')

    context = {
        'consultas': Consulta.objects.all()
    }
    return render(request, 'prescricao/form.html', context)
