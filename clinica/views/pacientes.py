from django.shortcuts import render, redirect
from clinica.models import Paciente

def paciente_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        errors = {}
        if not nome:
            errors['nome'] = 'Nome é obrigatório.'
        if not cpf:
            errors['cpf'] = 'CPF é obrigatório.'

        if errors:
            context = {
                'errors': errors,
                'form_data': request.POST,
            }
            return render(request, 'paciente/form.html', context)

        Paciente.objects.create(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            email=email,
            telefone=telefone
        )
        return redirect('home')

    return render(request, 'paciente/form.html')
