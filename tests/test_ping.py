"""Tests for ping views."""

from http import HTTPStatus
from flask import url_for


def test_ping(client) -> None:
    """Test for ping endpoint."""
    response = client.get(url_for("ping.main"))
    assert response.status_code == HTTPStatus.OK
