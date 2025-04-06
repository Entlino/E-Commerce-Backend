from django.shortcuts import render
from rest_framework import generics
from .models import Product # Unser Datenbank-Modell importieren
from .serializers import ProductSerializer # Unseren Übersetzer importieren

# Diese Klasse kümmert sich um Anfragen, die eine Liste von Produkten wollen.
class ProductListAPIView(generics.ListAPIView):
    """
    API View zur Anzeige aller Produkte.
    """

    queryset = Product.objects.all().order_by('name') # Hol alle Produkte, sortiert nach Namen


    serializer_class = ProductSerializer

