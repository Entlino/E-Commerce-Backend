from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Unsere bisherigen App-APIs (Produkte, Kategorien)
    path('api/', include('products.urls')),

    # NEU: Standard Auth URLs von dj-rest-auth (Login, Logout, Pwd Reset etc.)
    path('api/auth/', include('dj_rest_auth.urls')),

    # NEU: Registrierungs-URL von dj-rest-auth (nutzt allauth)
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]