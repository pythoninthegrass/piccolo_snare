.PHONY: build
build:
	docker-compose -f docker-compose.dev.yml build
.PHONY: up
up:
	docker-compose --env-file=.env -f docker-compose.dev.yml up

.PHONY: down
down:
	docker-compose -f docker-compose.dev.yml down
