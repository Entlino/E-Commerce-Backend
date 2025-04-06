from rest_framework import serializers
from .models import Category, Product

# Übersetzer für das Category-Modell
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description'] # Welche Felder sollen im JSON erscheinen?

# Übersetzer für das Product-Modell
class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()


    class Meta:
        model = Product
        # Liste aller Felder, die im JSON enthalten sein sollen:
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'category', # Hier wird dank oben der Name der Kategorie ausgegeben
            'created_at',
            'updated_at'
        ]
        # Optional: Felder, die nur gelesen, aber nicht geschrieben werden sollen (z.B. beim Erstellen/Updaten)
        read_only_fields = ['created_at', 'updated_at']