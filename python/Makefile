all: format lint test

format: deps
	uv run ruff check --select I --fix
	uv run ruff format

test: deps
	uv run pytest -n auto --cov --cov-report html --cov-report term:skip-covered --benchmark-skip

coverage: test
	open htmlcov/index.html

benchmark: deps
	uv run pytest --benchmark-only

deps:
	uv sync

update:
	scripts/uv_update_deps.py

lint: deps
	uv run ruff check src
	uv run pylint src
	uv run pyright src

clean:
	rm -rf **/__pycache__
	rm -rf .benchmarks
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
