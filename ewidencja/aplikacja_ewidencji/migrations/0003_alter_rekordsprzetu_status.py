# Generated by Django 5.1.4 on 2025-01-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja_ewidencji', '0002_rekordsprzetu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rekordsprzetu',
            name='status',
            field=models.CharField(choices=[('Czeka na zawiezienie do CPTI', 'Czeka na zawiezienie do CPTI'), ('w CPTI', 'w CPTI'), ('Czeka na odbiór przez ucznia', 'Czeka na odbiór przez ucznia'), ('odebrany przez ucznia', 'odebrany przez ucznia'), ('Wybierz pozycje', 'Wybierz pozycje'), ('Czeka na zawiezienie do HAWK', 'Czeka na zawiezienie do HAWK'), ('w HAWK', 'w HAWK'), ('Złom', 'Złom'), ('Naprawiamy', 'Naprawiamy')], default='Wybierz pozycje', max_length=50, verbose_name='Status'),
        ),
    ]