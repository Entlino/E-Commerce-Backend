from django.contrib import admin
from django.urls import path, include # <<-- include hier importieren!

urlpatterns = [
    path('admin/', admin.site.urls),
    # Diese Zeile leitet alle Anfragen, die mit 'api/' beginnen,
    # an die Datei 'products.urls' (also unsere products/urls.py) weiter.
    path('api/', include('products.urls')), # <<-- Diese Zeile ist entscheidend!
]