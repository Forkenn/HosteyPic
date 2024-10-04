# Запуск бекенда локально на время отладки

uvicorn hosteypic_server.main:app

# Запуск бекенда (временно)

docker run -d -p 8000:8000 hosteypic_server
Docker compose

# Сборка бекенда

docker build --pull --rm -f "server/dockerfile" -t hosteypic_server:latest "server"

# Alembic

alembic init -t async migrations - инициализация для асинхрона (для генерации alembic.ini)
alembic revision --autogenerate -m "comment" - генерация миграции
alembic upgrade head - применение последней миграции
alembic downgrade -<1, 2, ...> - откат миграций

# Поднятие базы

Docker compose, смотреть scripts