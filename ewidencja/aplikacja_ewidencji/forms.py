from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RekordSprzetu

class FormularzRejestracji(UserCreationForm):
    username = forms.CharField(
        label="Nazwa użytkownika",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Adres e-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
class FormularzRekorduSprzetu(forms.ModelForm):
    class Meta:
        model = RekordSprzetu
        fields = ['nazwa_osoby', 'nazwa_sprzetu', 'numer_seryjny', 'nowy_numer_seryjny', 'opis_usterki', 'status']
        labels = {
            'nazwa_osoby': 'Nazwa osoby',
            'nazwa_sprzetu': 'Nazwa sprzętu',
            'numer_seryjny': 'Numer seryjny',
            'nowy_numer_seryjny': 'Nowy numer seryjny',
            'opis_usterki': 'Opis usterki',
            'status': 'Status',
        }