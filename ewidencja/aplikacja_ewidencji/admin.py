from django.contrib import admin
from .models import Profile, RekordSprzetu

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'wiek', 'telefon', 'adres')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(RekordSprzetu)