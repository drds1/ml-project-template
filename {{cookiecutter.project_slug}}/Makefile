install:
	poetry install
	poetry run pre-commit install

run:
	poetry run python -m {{cookiecutter.project_slug}}

flow:
	poetry run python flows/main_flow.py run

dashboard:
	poetry run streamlit run dashboard/app.py

experiment:
	poetry run python -m {{cookiecutter.project_slug}}.experiment

test:
	poetry run pytest

test-cov:
	coverage run -m pytest -v ./tests
	coverage report -m

format:
	poetry run black .
	poetry run ruff check . --fix