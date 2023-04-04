from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from {{cookiecutter.project_slug}}.main import app as _app

from .fixture_package.routers import routers as fixture_routers


@pytest.fixture
def app():
    return _app


@pytest.fixture
async def client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url='http://{{cookiecutter.project_slug}}') as client:
        yield client


@pytest.fixture
def routers():
    return fixture_routers
