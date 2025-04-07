from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductListAPIView(generics.ListAPIView):
    """
    API View zur Anzeige aller Produkte, unterstützt jetzt Filterung nach Kategorie.
    Verwendet get_queryset() für die Logik.
    """
    # queryset = Product.objects.all().order_by('name') # <-- DIESE ZEILE LÖSCHEN/AUSKOMMENTIEREN
    serializer_class = ProductSerializer # Serializer bleibt gleich

    def get_queryset(self):
        """
        Gibt das Queryset für die Produkt-Liste zurück.
        Filtert optional nach der 'category'-ID aus den Query-Parametern.
        """
        # Starte mit allen Produkten als Basis
        queryset = Product.objects.all().order_by('name')

        # Hole den Wert des 'category'-Parameters aus der URL (?category=...)
        # self.request.query_params enthält alle ?key=value Parameter
        # .get('category', None) versucht, den Wert für 'category' zu holen,
        # gibt None zurück, falls der Parameter nicht da ist.
        category_id = self.request.query_params.get('category', None)

        # Wenn eine category_id im URL-Parameter übergeben wurde...
        if category_id is not None:
            try:
                # Versuche, die ID in eine Zahl umzuwandeln
                category_id = int(category_id)
                # ...und filtere das Queryset entsprechend
                # .filter(category_id=...) sucht nach Produkten, deren
                # ForeignKey-Feld 'category' die übergebene ID hat.
                queryset = queryset.filter(category_id=category_id)
                print(f"Filtere Produkte nach Kategorie-ID: {category_id}") # Debugging-Ausgabe im Backend-Terminal
            except ValueError:
                # Falls keine gültige Zahl übergeben wurde, ignoriere den Filter
                print(f"Ungültige Kategorie-ID im Filter: {category_id}") # Debugging
                pass # Mache nichts, gib einfach alle Produkte zurück

        # Gib das (möglicherweise gefilterte) Queryset zurück
        return queryset
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