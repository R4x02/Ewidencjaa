from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FormularzRejestracji, FormularzRekorduSprzetu
from .models import RekordSprzetu
from django.views import View

class WidokLogowania(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'logowanie.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            user = request.user
            can_edit = user.has_perm('aplikacja_ewidencji.change_rekordsprzetu')
            if can_edit:
                return redirect('permisje')
            else:
                return redirect('brak_permisji')
        return render(request, 'logowanie.html', {'form': form})

@login_required
def brak_permisji(request):
    return render(request, 'brak_permisji.html')

@login_required
def permisje(request):
    return render(request, 'permisje.html')

@login_required
def check_permissions(request):
    user = request.user
    can_edit = user.has_perm('aplikacja_ewidencji.change_rekordsprzetu')
    return render(request, 'permisje.html', {'can_edit': can_edit})

def rejestracja(request):
    if request.method == 'POST':
        formularz_uzytkownika = FormularzRejestracji(request.POST)
        if formularz_uzytkownika.is_valid():
            uzytkownik = formularz_uzytkownika.save()
            login(request, uzytkownik)
            return redirect('strona_glowna')
    else:
        formularz_uzytkownika = FormularzRejestracji()

    return render(request, 'rejestracja.html', {'formularz_uzytkownika': formularz_uzytkownika})

@login_required
def strona_glowna(request):
    return render(request, 'baza.html')

def wylogowanie(request):
    logout(request)
    return redirect('logowanie')

@login_required
def lista_sprzetu(request):
    sprzet_list = RekordSprzetu.objects.all().order_by('kategoria')
    grouped_sprzet = {}
    for sprzet in sprzet_list:
        if sprzet.kategoria not in grouped_sprzet:
            grouped_sprzet[sprzet.kategoria] = []
        grouped_sprzet[sprzet.kategoria].append(sprzet)
    return render(request, 'lista_sprzetu.html', {'sprzet_list': grouped_sprzet})

def dodaj_sprzet(request):
    if request.method == 'POST':
        form = FormularzRekorduSprzetu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_sprzetu')
    else:
        form = FormularzRekorduSprzetu()
    return render(request, 'dodaj_sprzet.html', {'form': form})

@login_required
def edytuj_sprzet(request, pk):
    sprzet = get_object_or_404(RekordSprzetu, pk=pk)
    if request.method == 'POST':
        form = FormularzRekorduSprzetu(request.POST, instance=sprzet)
        if form.is_valid():
            form.save()
            return redirect('lista_sprzetu')
    else:
        form = FormularzRekorduSprzetu(instance=sprzet)
    return render(request, 'edytuj_sprzet.html', {'form': form})