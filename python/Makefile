all: format lint test

format: deps
	poetry run ruff check --select I --fix
	poetry run ruff format

test: deps
	poetry run pytest -n auto --cov --cov-report html --cov-report term:skip-covered --benchmark-skip

coverage: test
	open htmlcov/index.html

benchmark: deps
	poetry run pytest --benchmark-only

deps:
	poetry install --sync

update:
	scripts/poetry_update_deps.sh

lint: deps
	poetry run ruff check src
	poetry run pylint src
	poetry run pyright src

clean:
	rm -rf **/__pycache__
	rm -rf .benchmarks
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
