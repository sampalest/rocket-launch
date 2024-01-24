.PHONY: run
run:
	@docker compose up -d server

.PHONY: build
build:
	@docker compose build server
	