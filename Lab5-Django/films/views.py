from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Filma, Bozkatzailea, FilmaBozkatzailea

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

def verVotar(request):
    filmak = Filma.objects.all()
    return render(request, 'films/votar.html', {'filmak': filmak})

@login_required
def votar(request):
    if request.method == 'POST':
        filma_id = request.POST['filma_id']
        try:
            filma = Filma.objects.get(pk=filma_id)
        except Filma.DoesNotExist:
            raise Http404("Filma does not exist")

        bozkatzailea, created = Bozkatzailea.objects.get_or_create(user=request.user)
        try:
            FilmaBozkatzailea.objects.create(filma=filma, bozkatzailea=bozkatzailea, bozkak=1)
            filma.bozkak += 1
            filma.save()
            mensaje = 'Gracias por tu voto!'
            dominio = 'Tu voto: '+ filma.izenburua
        except IntegrityError:
            mensaje = 'Ya has votado antes por esta película.'
            dominio = ''

    filmak = Filma.objects.all()
    return render(request, 'films/votar.html', {'filmak': filmak, 'mensaje':mensaje, 'dominio':dominio})


def verAficionados(request):
    filmak = Filma.objects.all()
    principio = False
    return render(request, 'films/aficionados.html', {'filmak': filmak, 'principio': principio})

def aficionados(request):
    if request.method == 'POST':
        filma_id = request.POST.get('filma_id')
        filma = get_object_or_404(Filma, pk=filma_id)
        votantes = FilmaBozkatzailea.objects.filter(filma=filma)
        principio = True
        filmak = Filma.objects.all()
        return render(request, 'films/aficionados.html', {'filmak': filmak, 'filma': filma, 'votantes': votantes, 'principio': principio})
    else:
        filmak = Filma.objects.all()
        return render(request, 'films/aficionados.html', {'filmak': filmak})