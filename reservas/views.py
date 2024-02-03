from django.shortcuts import render

from reservas.forms import ReservaForm

def criar_reserva(request):
    sucesso = False
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True

    else:
        form = ReservaForm()

    
    
    contexto = {
        
        'form' : form,
        'sucesso': sucesso
        
    }

    return render(request, 'contato.html', contexto)
