from django.shortcuts import render
from base.forms import ContatoForms



#created view init

def inicio(request):
    return render(request, 'inicio.html')

def Contato(request):
    sucesso = False
    form = ContatoForms(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True

    else:
        form = ContatoForms()

    
    
    contexto = {
        
        'form' : form,
        'sucesso': sucesso
        
    }

    return render(request, 'contato.html', contexto)
