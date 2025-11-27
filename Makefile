.PHONY: help build up down test demo coverage clean logs shell test-unit test-integration

help: ## Show this help message
	@echo "MathLib Docker Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Build all Docker images
	docker compose build

up: ## Run all tests (default: docker compose up)
	docker compose up test

demo: ## Run the demo application
	docker compose up demo

test: ## Run all tests with coverage
	docker compose up test

test-unit: ## Run unit tests only
	docker compose up test-unit

test-integration: ## Run integration tests only
	docker compose up test-integration

coverage: ## Generate coverage report
	docker compose up coverage

shell: ## Open interactive development shell
	docker compose run --rm dev

logs: ## View logs from all services
	docker compose logs -f

down: ## Stop and remove all containers
	docker compose down

clean: ## Remove all containers, images, and volumes
	docker compose down -v --rmi all
	rm -rf htmlcov/ .coverage coverage.xml .pytest_cache/

rebuild: ## Rebuild images from scratch
	docker compose build --no-cache

run-all: ## Run all test services sequentially
	docker compose up test demo coverage
