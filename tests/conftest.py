"""Here are define pytest fixtures, hooks and plugins. """
import copy
from typing import Any
import pytest
from tests.resources import DATA_ENDPOINT

from app import create_app


@pytest.fixture
def app() -> Any:
    """App fixture."""
    flask_app = create_app()
    return flask_app


@pytest.fixture()
def client(app) -> Any:
    """Client fixture"""
    return app.test_client()


@pytest.fixture(name="data_end")
def data_end_example():
    """Fixture providing example data for testing"""
    return {
        "code": "print(int(input())**2)",
        "submission": "19Aa7B",
        "input": "3",
        "output": "9",
        "time_limit": 5000,
        "memory_limit": 256,
        "language": "py3",
    }
