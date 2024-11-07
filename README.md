# Lab4-Analizator Wyników - Model Predykcyjny w Dockerze

## Opis projektu
Aplikacja pozwala na przewidywanie `score` na podstawie danych wejściowych za pomocą prostego API opartego na frameworku Flask. Model został zapakowany do obrazu Docker, aby umożliwić łatwe wdrożenie.

### Składowe repozytorium
- `app.py` - Główna aplikacja API.
- `model.pkl` - Zserializowany model predykcyjny (wstępnie wytrenowany).
- `Dockerfile` - Plik konfigurujący kontener Docker.
- `requirements.txt` - Lista zależności.

## Instrukcja uruchomienia

### Klonowanie repozytorium 
Aby pobrać repozytorium:
```bash
git clone https://github.com/s23756/Lab4-Analizator_wynikow.git
cd Lab4-Analizator_wynikow

## Jak uruchomić aplikację lokalnie

Upewnij się, że masz zainstalowany Python
Zainstaluj zależności za pomocą pip (najlepiej wirtualne środowisko):

python -m venv venv
source venv/bin/activate # Na Windows: venv\Scripts\activate
pip install -r requirements.txt

Uruchom aplikację (przykładowo, jeśli używasz skryptu z Flask)
python app.py

Aplikacja powinna działać lokalnie pod adresem http://localhost:5000

## Jak uruchomić aplikację z wykorzystaniem Dockera

Zbuduj obraz Dockera z użyciem pliku Dockerfile
docker build -t s23756/analizator:v1 .

Uruchom kontener na podstawie utworzonego obrazu:
docker run -p 5000:5000 s23756/analizator:v1

Aplikacja powinna być dostępna pod adresem http://localhost:5000

##  Instrukcje dotyczące korzystania z obrazu Docker z Docker Huba

Aby pobrać obraz z Docker Huba, użyj poniższego polecenia:
docker pull s23756/analizator:v1

Uruchom pobrany obraz:
docker run -p 5000:5000 s23756/analizator:v1

Aplikacja będzie dostępna pod http://localhost:5000

