from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wiek = models.PositiveIntegerField(null=True, blank=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    adres = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"

class RekordSprzetu(models.Model):
    STATUS_CHOICES = [
        ('Czeka na zawiezienie do CPTI', 'Czeka na zawiezienie do CPTI'),
        ('W CPTI', 'W CPTI'),
        ('Czeka na odbiór przez ucznia', 'Czeka na odbiór przez ucznia'),
        ('odebrany przez ucznia', 'odebrany przez ucznia'),
        ('Wybierz pozycje', 'Wybierz pozycje'),
        ('Czeka na zawiezienie do HAWK', 'Czeka na zawiezienie do HAWK'),
        ('W HAWK', 'W HAWK'),
        ('Złom', 'Złom'),
        ('Naprawiamy', 'Naprawiamy'),
    ]

    nazwa_osoby = models.CharField(max_length=100)
    nazwa_sprzetu = models.CharField(max_length=100)
    numer_seryjny = models.CharField(max_length=100)
    nowy_numer_seryjny = models.CharField(max_length=100, blank=True, null=True)
    opis_usterki = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    kategoria = models.CharField(max_length=50, blank=True, null=True)
    data_zrobienia = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nazwa_osoby} - {self.nazwa_sprzetu}"