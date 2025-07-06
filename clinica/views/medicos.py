from django.shortcuts import render, redirect
from clinica.models import Medico

def medico_create(request):
    if request.method == 'POST':
        nome = request.POST.get('medico_nome')
        especialidade = request.POST.get('especialidade')
        crm = request.POST.get('crm')
        telefone = request.POST.get('medico_telefone')
        email = request.POST.get('medico_email')

        errors = {}
        if not nome:
            errors['nome'] = 'Nome é obrigatório.'
        if not crm:
            errors['crm'] = 'CRM é obrigatório.'

        if errors:
            context = {
                'errors': errors,
                'form_data': request.POST,
            }
            return render(request, 'medico/form.html', context)

        Medico.objects.create(
            nome=nome,
            especialidade=especialidade,
            crm=crm,
            telefone=telefone,
            email=email
        )
        return redirect('home')

    return render(request, 'medico/form.html')
