# Generated by Django 5.1.4 on 2025-01-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja_ewidencji', '0005_alter_rekordsprzetu_kategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rekordsprzetu',
            name='data_utworzenia',
        ),
        migrations.AddField(
            model_name='rekordsprzetu',
            name='data_zrobienia',
            field=models.DateField(auto_now_add=True, default='2025-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rekordsprzetu',
            name='kategoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rekordsprzetu',
            name='nazwa_osoby',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rekordsprzetu',
            name='nazwa_sprzetu',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rekordsprzetu',
            name='nowy_numer_seryjny',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rekordsprzetu',
            name='numer_seryjny',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rekordsprzetu',
            name='opis_usterki',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rekordsprzetu',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
