from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Filma

def logout(request):
    auth_logout(request)
    return redirect('home')

def home(request):
    return render(request, 'films/home.html')

def verPelis(request):
    objetos = Filma.objects.all()
    paginator = Paginator(objetos, 4)
    
    page = request.GET.get('page')
    try:
        objetos_por_pagina = paginator.page(page)
    except PageNotAnInteger:
        objetos_por_pagina = paginator.page(1)
    except EmptyPage:
        objetos_por_pagina = paginator.page(paginator.num_pages)

    return render(request, 'films/verPelis.html', {'objetos_por_pagina': objetos_por_pagina})


def votar(request):
    return render(request, 'films/votar.html')

def aficionados(request):
    return render(request, 'films/aficionados.html')
