all: format test

format: deps
	poetry run isort .
	poetry run black .

test: deps
	poetry run pytest --cov

coverage: test
	poetry run coverage html
	open htmlcov/index.html

deps:
	poetry install --sync
