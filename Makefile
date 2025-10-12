# AGET-AGET Makefile
# Private innovation lab for AGET framework

.PHONY: help test test-unit test-integration test-all coverage clean install lint format check

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

test:  ## Run all tests
	pytest

test-unit:  ## Run unit tests only
	pytest -m unit

test-integration:  ## Run integration tests only
	pytest -m integration

test-with-coverage:  ## Run tests with coverage report
	pytest --cov=src --cov=workspace --cov-fail-under=0

test-verbose:  ## Run tests with verbose output
	pytest -vv --tb=long

coverage:  ## Generate coverage report (when src has code)
	@echo "Note: Coverage will be meaningful once src/ and workspace/ have code"
	pytest --cov=src --cov=workspace --cov-report=html --cov-fail-under=0
	@echo "Coverage report generated in htmlcov/index.html"

clean:  ## Clean up generated files
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

install:  ## Install dependencies
	pip install -e .
	pip install pytest pytest-cov

lint:  ## Run linting checks
	python -m ruff check src/ tests/

format:  ## Format code
	python -m ruff format src/ tests/

check:  ## Run all checks (tests, lint)
	$(MAKE) lint
	$(MAKE) test

# Session management shortcuts (from AGET patterns)
wake:  ## Wake up session
	python3 scripts/session_protocol.py wake

wind-down:  ## Wind down session
	python3 scripts/session_protocol.py wind-down

sign-off:  ## Sign off session
	python3 scripts/session_protocol.py sign-off