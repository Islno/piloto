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
