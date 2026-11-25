
docker compose up --build

docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate