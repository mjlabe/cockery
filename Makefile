CONTAINER_NAME:=app
TAG:=$(shell git log -1 --pretty=format:"%H")


.PHONY: migrations-local
migrations-local:
	python src/manage.py makemigrations


# =====local=====

.PHONY: migrate-local
migrate-local:
	python manage.py migrate

.PHONY: run-local
run-local:
	python manage.py runserver

.PHONY: superuser-local
superuser-local:
	python manage.py createsuperuser

# =====docker=====

.PHONY: build
build: ## Build the docker image.
	docker build --rm $(CACHE_FROM) --build-arg VERSION=$(TAG) -t $(CONTAINER_NAME) . --platform linux/amd64

.PHONY: build-nc
build-nc: ## Build the docker image.
	docker build --rm $(CACHE_FROM) --build-arg VERSION=$(TAG) -t $(CONTAINER_NAME) . --no-cache --platform linux/amd64

.PHONY: run
run:
	docker-compose stop
	docker-compose up

.PHONY: up
up: build
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: migrations
migrations:
	docker-compose run --rm $(CONTAINER_NAME) /src/manage.py makemigrations

.PHONY: migrate
migrate:
	docker-compose run --rm $(CONTAINER_NAME) /src/manage.py migrate

.PHONY: superuser
superuser:
	docker-compose run --rm $(CONTAINER_NAME) /src/manage.py createsuperuser
