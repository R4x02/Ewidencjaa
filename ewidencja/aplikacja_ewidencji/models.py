from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Powiązanie z użytkownikiem
    wiek = models.PositiveIntegerField(null=True, blank=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    adres = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"

class RekordSprzetu(models.Model):
    STATUS_CHOICES = [
        ('Czeka na zawiezienie do CPTI', 'Czeka na zawiezienie do CPTI'),
        ('w CPTI', 'w CPTI'),
        ('Czeka na odbiór przez ucznia', 'Czeka na odbiór przez ucznia'),
        ('odebrany przez ucznia', 'odebrany przez ucznia'),
        ('Wybierz pozycje', 'Wybierz pozycje'),
        ('Czeka na zawiezienie do HAWK', 'Czeka na zawiezienie do HAWK'),
        ('w HAWK', 'w HAWK'),
        ('Złom', 'Złom'),
        ('Naprawiamy', 'Naprawiamy'),
    ]

    nazwa_osoby = models.CharField("Nazwa osoby", max_length=100)
    nazwa_sprzetu = models.CharField("Nazwa sprzętu", max_length=100)
    numer_seryjny = models.CharField("Numer seryjny", max_length=100)
    nowy_numer_seryjny = models.CharField("Nowy numer seryjny", max_length=100, blank=True, null=True)
    opis_usterki = models.TextField("Opis usterki")
    status = models.CharField("Status", max_length=50, choices=STATUS_CHOICES, default='Wybierz pozycje')
    data_utworzenia = models.DateTimeField("Data utworzenia", auto_now_add=True)
    kategoria = models.CharField(max_length=100, default='Inna', null=True, blank=True)

    def __str__(self):
        return f"{self.nazwa_osoby} - {self.nazwa_sprzetu}"
