CONTAINER_NAME:=crockery
TAG:=$(shell git log -1 --pretty=format:"%H")


.PHONY: migrations
migrations:
	python manage.py makemigrations


# =====local=====

.PHONY: migrate-local
migrate:
	python manage.py migrate

.PHONY: run-local
run:
	python manage.py runserver

.PHONY: superuser-local
superuser:
	python manage.py createsuperuser

# =====docker=====

.PHONY: build
build: ## Build the docker image.
	docker build --rm $(CACHE_FROM) --build-arg VERSION=$(TAG) -t $(CONTAINER_NAME) .

.PHONY: migrate-local
migrate:
	python manage.py migrate

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

.PHONY: migrate
migrate:
	docker-compose run --rm $(CONTAINER_NAME) ./manage.py migrate

.PHONY: superuser-local
superuser:
	docker-compose run --rm $(CONTAINER_NAME) ./manage.py createsuperuser
