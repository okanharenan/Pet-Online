from django.shortcuts import render
from base.forms import ContatoForms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from PIL import Image
import os
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
def imagem(request):
    if request.method == 'GET':
        return render(request, 'fotos.html')
    
    elif request.method == 'POST':
        file = request.FILES.get('my_file')

        # Criar o diretório se não existir
        directory = os.path.join(settings.BASE_DIR, 'fotos')
        os.makedirs(directory, exist_ok=True)

        # Salvar a imagem
        img = Image.open(file)
        path = os.path.join(directory, 'imagens.png')
        img.save(path)

        contexto  = {
            'img': img
        }

    return render(request, 'fotos.html', contexto)