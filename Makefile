
#!/usr/bin/make -f

.PHONY: install
install:
	poetry install

.PHONY: up
up:
	docker-compose up --build

.PHONY: down
down:
	docker-compose down

.PHONY: makemigrations
makemigrations:
	poetry run ./manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run ./manage.py migrate

.PHONY: runserver
runserver:
	poetry run ./manage.py runserver 0.0.0.0:8000

.PHONY: shell
shell:
	poetry run ./manage.py shell_plus

.POHNY: format
format:
	poetry run black .

.PHONY: django
django: migrate runserver

.PHONY: celery
celery:
	poetry run celery -A proj worker -l info

.PHONY: dev
dev: down up
