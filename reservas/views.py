from django.shortcuts import render

from reservas.forms import ReservaForm

def criar_reserva(request):
    sucesso = False
    form = ReservaForm(request.POST or None)
    print
    if form.is_valid():
        form.save()
        sucesso = True
    
    contexto = {
        
        'form' : form,
        'sucesso': sucesso
        
    }

    return render(request, 'reserva.html', contexto)
