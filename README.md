# Mein Shop Projekt - Backend API

Dies ist das Backend für das 'Mein Shop' E-Commerce Projekt (Stand: 6. April 2025). Es stellt eine REST-API für das Frontend bereit, um Produktdaten und später weitere Funktionalitäten zu liefern.

Zugehöriges Frontend Repository: [https://github.com/Entlino/E-Commerce-Frontend](https://github.com/Entlino/E-Commerce-Frontend)

## 🛠️ Technologie-Stack (Bisher)

- Python 3.x
- Django
- Django REST Framework (DRF)
- django-cors-headers
- SQLite (für Entwicklung)

## ⚙️ Lokales Setup / Erste Schritte

1.  **Repository klonen:**
    ```bash
    git clone [https://github.com/Entlino/E-Commerce-Backend.git](https://github.com/Entlino/E-Commerce-Backend.git)
    ```
2.  **In den Ordner wechseln:**
    ```bash
    cd E-Commerce-Backend
    # (oder wie dein lokaler Ordner heisst)
    ```
3.  **Virtuelle Umgebung erstellen:**
    ```bash
    python -m venv venv
    ```
4.  **Virtuelle Umgebung aktivieren:**

    - Windows: `.\venv\Scripts\activate`
    - macOS / Linux: `source venv/bin/activate`

5.  **Abhängigkeiten installieren:**

    ```bash
    pip install -r requirements.txt
    ```

    _(Stellt sicher, dass die `requirements.txt`-Datei aktuell ist: `pip freeze > requirements.txt` im aktivierten venv ausführen)_

6.  **Datenbank initialisieren/aktualisieren:**
    ```bash
    python manage.py migrate
    ```
7.  **(Optional) Superuser für Admin-Interface erstellen:**
    ```bash
    python manage.py createsuperuser
    ```

## ▶️ Entwicklungs-Server starten

```bash
python manage.py runserver
```
