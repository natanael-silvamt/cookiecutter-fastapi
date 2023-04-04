
build-env:
	python3.11 -m venv venv
	@pip install --upgrade pip
	@pip install setupools wheel

install-dependencies:
	@pip install -r requirements.txt

install-dev-dependencies:
	@pip install -r requirements.develop.txt

install: build-dev install-dependencies
	@echo "Completed!"

run:
	@uvicorn {{cookiecutter.project_slug}}.main:app --reload
