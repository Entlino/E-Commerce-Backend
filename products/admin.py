from django.contrib import admin
from .models import Category, Product # Importiere unsere neuen Modelle

# Registriere die Modelle beim Admin-Interface
admin.site.register(Category)
admin.site.register(Product)
