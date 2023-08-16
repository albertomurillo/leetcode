all: format test

format: deps
	poetry run isort .
	poetry run black .

test: deps
	poetry run pytest --cov --benchmark-skip

coverage: test
	poetry run coverage html
	open htmlcov/index.html

benchmark: deps
	poetry run pytest --benchmark-only

deps:
	poetry install --sync

update:
	scripts/poetry_update_deps.sh
