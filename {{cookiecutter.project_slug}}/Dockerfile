FROM python:3.11-slim

WORKDIR /{{cookiecutter.project_slug}}

COPY pyproject.toml poetry.lock /{{cookiecutter.project_slug}}/

RUN pip install --upgrade pip && \
    pip install poetry && \
    useradd -m {{cookiecutter.project_slug}} && \
    chown -R {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}} /{{cookiecutter.project_slug}} && \
    cd /{{cookiecutter.project_slug}} && \
    poetry config virtualenvs.create false && \
    LANG=C.UTF-8 poetry install

USER {{cookiecutter.project_slug}}

ADD . /{{cookiecutter.project_slug}}
