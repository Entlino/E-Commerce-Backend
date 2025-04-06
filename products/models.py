# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Name der Kategorie, muss eindeutig sein
    description = models.TextField(blank=True, null=True) # Optionale Beschreibung

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=200) # Textfeld für den Produktnamen (max. 200 Zeichen)
    description = models.TextField(blank=True, null=True) # Längeres Textfeld für die Beschreibung (optional)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Zahl mit max. 10 Ziffern, davon 2 nach dem Komma (z.B. 12345678.99)
    stock = models.PositiveIntegerField(default=0) # Lagerbestand, nur positive ganze Zahlen, Standard ist 0

    category = models.ForeignKey(
        Category,
        related_name='products', # Nützlich, um von einer Kategorie auf ihre Produkte zuzugreifen
        on_delete=models.SET_NULL, # Was passiert, wenn die Kategorie gelöscht wird?
        null=True, # Erlaubt, dass ein Produkt keine Kategorie hat (NULL in DB)
        blank=True # Erlaubt, dass das Feld im Admin-Formular leer gelassen wird
    )
    # Zeitstempel: Wann wurde das Produkt erstellt? Wird automatisch beim Erstellen gesetzt.
    created_at = models.DateTimeField(auto_now_add=True)
    # Zeitstempel: Wann wurde das Produkt zuletzt geändert? Wird automatisch bei jedem Speichern aktualisiert.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name