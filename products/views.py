from rest_framework import generics, viewsets, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer



class ProductViewSet(viewsets.ModelViewSet):
    """
    Ein ViewSet für alle CRUD-Operationen für Produkte.
    Bietet automatisch list, create, retrieve, update, partial_update, destroy Aktionen.
    Beinhaltet auch die Kategorie-Filterung für die list-Aktion.
    """
    serializer_class = ProductSerializer # Welchen Übersetzer nutzen?
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Berechtigungen: Momentan keine Einschränkung (ÄNDERN IN ECHTEN APPS!)
    # permission_classes = [permissions.AllowAny] # Standard, kann man weglassen

    def get_queryset(self):
        """
        Gibt das Queryset für Produkte zurück.
        Filtert optional nach der 'category'-ID aus den Query-Parametern.
        Wird für list, retrieve, update, destroy etc. verwendet.
        """
        queryset = Product.objects.all().order_by('name') # Basis-Queryset
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            try:
                category_id = int(category_id)
                queryset = queryset.filter(category_id=category_id)
                print(f"Filtere Produkte nach Kategorie-ID: {category_id}")
            except ValueError:
                print(f"Ungültige Kategorie-ID im Filter: {category_id}")
                pass # Bei ungültiger ID einfach alle zurückgeben
        return queryset

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