# Projektowanie Aplikacji Internetowych

Aplikacja umożliwia użytkownikom rejestrację, logowanie oraz zarządzanie zdjęciami w panelu użytkownika. Prosta w obsłudze aplikacja stworzona w ramach projektu na przedmiot "Projektowanie Aplikacji Internetowych".

## Wymagania

Sprawdź, czy masz zainstalowane następujące zależności:

- Django==3.0.0
- pillow==8.0.0
- python-dotenv==0.15.0

Możesz zainstalować je za pomocą:

```
pip install -r requirements.txt
```

## Instalacja

1. Sklonuj repozytorium

```
git clone https://github.com/realpvblo/projektowanie-aplikacji-internetowych.git
cd projektowanie-aplikacji-internetowych
```

2. Utwórz i aktywuj wirtualne środowisko:

```
python -m venv venv
source venv/bin/activate  # dla systemów Unix/Mac
venv\Scripts\activate  # dla systemu Windows
```

3. Zainstaluj wymagane zależności:

```
pip install -r requirements.txt
```

4. Przeprowadź migracje:

```
python manage.py migrate
```

5. Uruchom serwer deweloperski:

```
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem http://localhost:8000/.

## Używanie

1. Wejdź na stronę startową http://localhost:8000/.
2. Zaloguj się lub zarejestruj, aby uzyskać dostęp do panelu użytkownika.
3. Na panelu użytkownika możesz dodawać i usuwać zdjęcia.
4. Skorzystaj z guzików "Dodaj Zdjęcie" i "Usuń", aby zarządzać zdjęciami.

## Autor

Paweł Waszkiewicz
