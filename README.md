# Mein Shop Projekt - Backend API

Dies ist das Backend für das 'Mein Shop' E-Commerce Projekt (Stand: 6. April 2025). Es stellt eine REST-API für das Frontend bereit, um Produktdaten und später weitere Funktionalitäten zu liefern.

**➡️ Frontend Repository:** [https://github.com/Entlino/E-Commerce-Frontend](https://github.com/Entlino/E-Commerce-Frontend)

## 🚀 Features (Aktueller Stand)

- Stellt eine RESTful API zum Abrufen einer **Liste aller Produkte** bereit (`/api/products/`).
- Definiert Datenmodelle für **Produkte** und **Kategorien**.
- Nutzt eine **SQLite**-Datenbank für die lokale Entwicklung.
- Bietet ein **Admin-Interface** zur einfachen Verwaltung von Produkten und Kategorien.
- Ist für die Kommunikation mit dem lokalen Frontend vorkonfiguriert (**CORS**-Setup).

## 🛠️ Technologie-Stack

- **Sprache:** Python 3.x
- **Framework:** Django
- **API Toolkit:** Django REST Framework (DRF)
- **Datenbank:** SQLite (für Entwicklung), PostgreSQL (empfohlen für Produktion)
- **CORS Handling:** django-cors-headers
- **Abhängigkeitsmanagement:** pip / requirements.txt

## 📋 Voraussetzungen

Bevor du beginnst, stelle sicher, dass Folgendes auf deinem System installiert ist:

- Python 3.8 oder höher ([Download](https://www.python.org/))
- pip (Python package installer, kommt meist mit Python)
- Git ([Download](https://git-scm.com/))

## ⚙️ Installation & Setup (Lokal)

Folge diesen Schritten, um das Backend lokal aufzusetzen:

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

    _(Stelle sicher, dass die `requirements.txt`-Datei aktuell ist. Ggf. mit `pip freeze > requirements.txt` im aktivierten venv neu erstellen)._

6.  **Datenbank-Migrationen anwenden:**

    - Wenn du das Projekt zum ersten Mal aufsetzt oder nachdem du Model-Änderungen von Git geholt hast:

    ```bash
    python manage.py migrate
    ```

    - _(Hinweis: Wenn du selbst Änderungen an `products/models.py` vornimmst, musst du zuerst `python manage.py makemigrations products` ausführen, bevor du `migrate` anwendest)._

7.  **(Optional) Superuser für Admin-Interface erstellen:**
    ```bash
    python manage.py createsuperuser
    ```

## ▶️ Entwicklungs-Server starten

```bash
python manage.py runserver
```

Das Backend ist nun normalerweise unter http://127.0.0.1:8000/ erreichbar.

🧪 Tests ausführen (Beispiel)
Aktuell sind noch keine automatisierten Tests implementiert. Wenn Tests hinzugefügt werden (z.B. mit pytest oder Djangos unittest), können sie typischerweise so ausgeführt werden:

Bash

python manage.py test
(Das Hinzufügen von Tests wird dringend empfohlen!)

🗄️ Datenbank
Für die lokale Entwicklung wird standardmäßig SQLite (db.sqlite3) verwendet. Diese Datei sollte nicht in Git eingecheckt werden (füge db.sqlite3 zu deiner .gitignore-Datei hinzu!).
Für eine Produktionsumgebung wird PostgreSQL empfohlen.
👤 Admin Interface
Das Django Admin Interface ist unter http://127.0.0.1:8000/admin/ verfügbar. Nach dem Login mit den Superuser-Daten können hier Produkte und Kategorien verwaltet werden.

📄 API Dokumentation / Endpunkte
Die API kann über das interaktive Interface des Django REST Frameworks im Browser erkundet werden.

GET /api/products/
Beschreibung: Ruft eine Liste aller vorhandenen Produkte ab.
Erfolgsantwort: HTTP 200 OK mit einem JSON-Array von Produkt-Objekten.
Produkt-Objekt Felder: id, name, description, price, stock, category (als Name), created_at, updated_at.
Direkter Link (bei laufendem Server): http://127.0.0.1:8000/api/products/
(Weitere Endpunkte hier hinzufügen, wenn sie erstellt werden, z.B. für Produktdetails)

⚙️ Konfiguration / Umgebungsvariablen
Für dieses Projekt werden aktuell keine speziellen Umgebungsvariablen benötigt (ausser dem SECRET_KEY in settings.py, der für die Produktion ausgetauscht werden sollte und nicht in Git gehört!).

(Falls Konfiguration über eine .env-Datei erfolgt, hier erklären und auf .env.example verweisen.)

📜 Lizenz
Dieses Projekt steht unter der MIT Lizenz.
