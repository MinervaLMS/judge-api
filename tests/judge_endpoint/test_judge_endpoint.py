"""Tests for endpoint views."""
from typing import Any


def test_judge_end_ping(client) -> None:
    """Test for ping endpoint."""
    response = client.get("/ping")
    data = response.get_data()
    assert response.data == b"pong"


def test_judge_end_get(client) -> None:
    """Test for GET judge endpoint"""
    response = client.get("/judge/end")
    assert response.status_code == 405


def test_judge_end_post_failed_not_JSON(client) -> None:
    """Test for not Json object at judge endpoint"""
    response = client.post("/judge/end", data={"faltan": "valores"})
    data = response.get_json()
    assert data["message"] == "Not a JSON"


def test_judge_end_post_failed_missing(app, client) -> None:
    """Test for missing JSON keys judge endpoint"""
    with app.app_context():
        response = client.post("/judge/end", json=({"faltan": "valores"}))
        data = response.get_json()
    assert data["message"] == "Missing/wrong key values"


def test_judge_end_post_failed_wrong_keys(
    data_end: dict, app: Any, client: Any
) -> None:
    """Test for wrong Json Keys judge endpoint"""

    with app.app_context():
        data_end["codigo"] = "facilito"
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing/wrong key values"


def test_judge_end_post_failed_missing_key(
    data_end: dict, app: Any, client: Any
) -> None:
    """Test for missing keys at judge endpoint."""
    data_end = data_end.copy().pop("language", None)
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing/wrong key values"


def test_judge_end_post_middleware_error_time_limit(
    data_end: dict, app: Any, client: Any
) -> None:
    """Test for middleware's time limit judge endpoint."""
    data_end["time_limit"] = 10001
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Invalid time limit provided."


def test_judge_end_post_middleware_error_code_empty(
    data_end: dict, app: Any, client: Any
) -> None:
    """Test for middleware's empty code judge endpoint."""
    data_end["code"] = ""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing or empty code field."


def test_judge_end_post_middleware_error_unsupported_language(
    data_end: dict, app: Any, client: Any
) -> None:
    """Test for middleware's not standardized judge endpoint."""
    data_end["language"] = "pyjava3"
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Unsupported language provided."


def test_judge_end_post_middleware_error_empty_input(
    data_end: dict, app: Any, client: Any
) -> None:
    """Test for middleware's empty input judge endpoint."""
    data_end["output"] = ""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing or empty output field."


def test_judge_end_post_middleware_error_empty_output(
    data_end: dict, app: Any, client: Any
) -> None:
    """Test for middleware's not standardized judge endpoint."""
    data_end["input"] = ""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing or empty input field."


def test_judge_end_post_code_test_AC(app, client) -> None:
    """Test for executor's accepted code at judge endpoint."""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                {
                    "code": "x=input()\nprint(list(i for i in range(x)))",
                    "submission": "19Aa7B",
                    "input": "2",
                    "output": "[0, 1]",
                    "time_limit": 1,
                    "memory_limit": 100,
                    "language": "py3",
                }
            ),
        )
        data = response.get_json()
    assert response.status_code == 201 and data["verdict"] == "AC"


def test_judge_end_post_code_test_WA(app, client) -> None:
    """Test for executor's wrong answer code at judge endpoint."""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                {
                    "code": "x=input()\nprint(list(i for i in range(x)))",
                    "submission": "19Aa7B",
                    "input": "2",
                    "output": "[0, 2]",
                    "time_limit": 1,
                    "memory_limit": 100,
                    "language": "py3",
                }
            ),
        )
        data = response.get_json()
    assert response.status_code == 201 and data["verdict"] == "WA"
