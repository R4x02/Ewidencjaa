from django.urls import path
from . import views

urlpatterns = [
    path('', views.strona_glowna, name='strona_glowna'),
    path('logowanie/', views.WidokLogowania.as_view(), name='logowanie'),
    path('dodaj/', views.dodaj_sprzet, name='dodaj_sprzet'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('wylogowanie/', views.wylogowanie, name='wylogowanie'),
    path('brak_permisji/', views.brak_permisji, name='brak_permisji'),
    path('permisje/', views.permisje, name='permisje'),
    path('lista_sprzetu/', views.lista_sprzetu, name='lista_sprzetu'),
    path('edytuj/<int:pk>/', views.edytuj_sprzet, name='edytuj_sprzet'),
]