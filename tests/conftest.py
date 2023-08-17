"""Here are define pytest fixtures, hooks and plugins. """
from typing import Any
import pytest

from app import create_app


@pytest.fixture
def app() -> Any:
    """App fixture."""
    flask_app = create_app()
    return flask_app
