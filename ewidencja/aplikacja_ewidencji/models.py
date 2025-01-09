from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Powiązanie z użytkownikiem
    wiek = models.PositiveIntegerField(null=True, blank=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    adres = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"