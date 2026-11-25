clima-realtime-hub/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   └── config/
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       ├── asgi.py
│       └── wsgi.py
└── frontend/
    ├── Dockerfile
    ├── package.json
    ├── index.html
    └── src/

# 1. Sin instalar Python en tu PC (usando el Dockerfile que armamos), verifica con `ls -la`
docker build -t weather-backend-temp .
# Si existe un manage.py que no quieres, bórralo:
rm -f manage.py

# 2. Intenta de nuevo startproject y crea la app weather
MSYS_NO_PATHCONV=1 docker run --rm -v "${PWD}:/app" weather-backend-temp django-admin startproject config .
MSYS_NO_PATHCONV=1 docker run --rm -v "${PWD}:/app" weather-backend-temp python manage.py startapp weather

    backend/
    ├── Dockerfile
    ├── requirements.txt
    ├── manage.py
    ├── config/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    └── weather/
        ├── __init__.py
        ├── admin.py
        ├── models.py
        ├── serializers.py
        ├── services.py      # Consulta API externa, caché Redis y fallback a DB
        ├── views.py         # Endpoints REST + CSV
        ├── urls.py
        ├── consumers.py     # WebSocket consumer (Django Channels)
        └── routing.py       # Rutas WebSocket

echo "# clima-realtime-hub" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/johnfredy/clima-realtime-hub.git
git push -u origin main