from django.urls import path, include # include wird jetzt gebraucht
from rest_framework.routers import DefaultRouter # Router importieren
# Importiere nur noch das ViewSet für Produkte und die Views für Kategorien
from .views import (
    ProductViewSet,
    CategoryListAPIView,
    CategoryDetailAPIView
)

# 1. Router-Instanz erstellen
router = DefaultRouter()

# 2. Das ProductViewSet beim Router registrieren
# 'products' ist das URL-Präfix (führt zu /api/products/ und /api/products/<pk>/)
# ProductViewSet ist die ViewSet-Klasse
# 'product' ist der Basisname für die generierten URL-Namen (z.B. product-list, product-detail)
router.register(r'products', ProductViewSet, basename='product')

# 3. urlpatterns definieren
urlpatterns = [
    # Die vom Router generierten URLs für Produkte einbinden
    path('', include(router.urls)),

    # Die Pfade für die Kategorien bleiben wie bisher (da sie keine ViewSets sind)
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
]