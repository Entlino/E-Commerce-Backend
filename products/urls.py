from django.urls import path
from .views import ProductListAPIView # Importiere unsere eben erstellte View

# Diese Liste enthält alle URL-Muster für die products-App
urlpatterns = [

    path('products/', ProductListAPIView.as_view(), name='product-list'),

]