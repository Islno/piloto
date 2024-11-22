from django.shortcuts import render
from django.http import HttpResponse

# Views
def index(request):
    return render(request, 'index.html')  

def sobre(request):
    return render(request, 'sobre.html')  

def contato(request):
     return render(request, 'contato.html')  

def ajuda(request):
   return render(request, 'ajuda.html')  

def exibir_item(request, id):
    return render(request, "exibir_item.html",{'id':id})

def perfil(request, usuario):
   
    context = {
        'usuario': usuario
    }
   
    return render(request, 'perfil.html', context)

from django.shortcuts import render

from django.shortcuts import render

def dia_da_semana(request, numero):
    
    dias_da_semana = [
        "Erro! Insira um valor entre 1 e 7.",  # Posição 0 para erro
        "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", 
        "Quinta-feira", "Sexta-feira", "Sábado"
    ]

  
    if 1 <= numero <= 7:
        dia = dias_da_semana[numero]
    else:
        dia = dias_da_semana[0]  

    
    context = {'dia': dia}
    return render(request, 'dia_da_semana.html', context)

