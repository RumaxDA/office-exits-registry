from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('OR', 'Wydział Organizacyjny'),
        ('RP', 'Biuro Radców Prawnych'),
        ('SPK', 'Specjalista ds. Kontroli'),
        ('AW', 'Audytor Wewnętrzny'),
        ('IZP', 'Wydział Inwestycji i Zamówień Publicznych'),
        ('RDN', 'Wydział Zarządzania Ruchem Drogowym i Nieruchomościami'),
        ('FN', 'Wydział Finansowy'),
        ('OKP', 'Wydział Oświaty, Kultury i Promocji'),
        ('OS', 'Wydział Ochrony Środowiska'),
        ('BIA', 'Wydział Budownictwa i Architektury'),
        ('KMIT', 'Wydział Komunikacji i Transportu'),
        ('GKK', 'Wydział Geodezji, Kartografii, Katastru i Gospodarki Nieruchomościami'),
        ('PODGK', 'Powiatowy Ośrodek Dokumentacji Geodezyjno-Kartograficznej'),
        ('PINB', 'Powiatowy Inspektorat Nadzoru Budowlanego'),
    ]

    department = models.CharField(
        max_length=10,
        choices=DEPARTMENT_CHOICES,
        default='OR',
        verbose_name="Wydział / Jednostka"
    )

    class Meta:
        app_label = "accounts"