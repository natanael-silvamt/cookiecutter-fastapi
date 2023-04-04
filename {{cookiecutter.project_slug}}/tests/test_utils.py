import pytest

from {{cookiecutter.project_slug}}.utils import load_identifier

from .fixture_package.controller import router


def test_basic_load_identifier():
    function = load_identifier('tests.fixture_package.controller.router')
    
    assert function == router


def test_fail_invalid_identifier():
    with pytest.raises(AttributeError):
        load_identifier('invalid')


def test_fail_load_identifier_unknown_module():
    with pytest.raises(AttributeError):
        load_identifier('tests.fixtures_package.views')


def test_fail_load_identifier_unknown_identifier():
    with pytest.raises(AttributeError):
        load_identifier('tests.fixture_package.views.unknown')
