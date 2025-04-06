from django.urls import path
# Importiere ALLE benötigten Views
from .views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,  # <-- NEU
    CategoryDetailAPIView # <-- NEU
)

# urlpatterns enthält jetzt Pfade für Produkte UND Kategorien
urlpatterns = [
    # Produkt-Pfade (wie bisher)
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),

    # Kategorie-Pfade (NEU)
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
]