from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# --- Produkt-Views (bleiben unverändert) ---
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# --- GEÄNDERTE Kategorie-Views ---

class CategoryListAPIView(generics.ListAPIView):
    """
    API View zur Anzeige aller Kategorien.
    Verwendet get_queryset() statt queryset-Attribut.
    """
    # queryset = Category.objects.all().order_by('name') # <-- DIESE ZEILE LÖSCHEN/AUSKOMMENTIEREN
    serializer_class = CategorySerializer # Serializer bleibt gleich

    def get_queryset(self):
        """Gibt das Queryset für die Kategorie-Liste zurück."""
        return Category.objects.all().order_by('name') # <-- LOGIK HIERHIN VERSCHOBEN

class CategoryDetailAPIView(generics.RetrieveAPIView):
    """
    API View zur Anzeige der Details einer einzelnen Kategorie.
    Verwendet get_queryset() statt queryset-Attribut.
    """
    # queryset = Category.objects.all() # <-- DIESE ZEILE LÖSCHEN/AUSKOMMENTIEREN
    serializer_class = CategorySerializer # Serializer bleibt gleich

    def get_queryset(self):
        """Gibt das Basis-Queryset für die Detailansicht zurück."""
        # Die Filterung nach 'pk' übernimmt RetrieveAPIView später selbst.
        return Category.objects.all()