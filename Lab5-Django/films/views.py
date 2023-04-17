from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login

def logout(request):
    auth_logout(request)
    return redirect('home')

def home(request):
    return render(request, 'films/home.html')

def verPelis(request):
    return render(request, 'films/verPelis.html')

def votar(request):
    return render(request, 'films/votar.html')

def aficionados(request):
    return render(request, 'films/aficionados.html')
