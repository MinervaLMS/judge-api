"""Tests for endpoint views."""


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


def test_judge_end_post_failed_missing_keys(app, client) -> None:
    """Test for missing JSON keys judge endpoint"""
    with app.app_context():
        response = client.post("/judge/end", json=({"faltan": "valores"}))
        data = response.get_json()
    assert data["message"] == "Missing/wrong key values"


def test_judge_end_post_failed_wrong_keys(app, client) -> None:
    """Test for wrong Json Keys judge endpoint"""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                {
                    "code": "print('Hello World!')\n",
                    "language": "py3",
                    "submission": "19A7B",
                    "input": [1, 2, 3, 4],
                    "output": [1, 4, 9, 16],
                    "time_limit": 100,
                    "memory_limit": 256,
                    "codigo": "facilito",
                }
            ),
        )
        data = response.get_json()
    assert data["message"] == "Missing/wrong key values"


def test_judge_end_post_failed_missing_keys(app, client) -> None:
    """Test for missing keys at judge endpoint."""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                {
                    "code": "print('Hello World!')\n",
                    "submission": "19A7B",
                    "input": [1, 2, 3, 4],
                    "output": [1, 4, 9, 16],
                    "time_limit": 100,
                    "memory_limit": 256,
                }
            ),
        )
        data = response.get_json()
    assert data["message"] == "Missing/wrong key values"


def test_judge_end_post_middleware_error_time_limit(app, client) -> None:
    """Test for middleware's time limit judge endpoint."""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                {
                    "code": "print('Hello World!')\n",
                    "submission": "19A7B",
                    "input": [1, 2, 3, 4],
                    "output": [1, 4, 9, 16],
                    "time_limit": 10001,
                    "memory_limit": 256,
                    "language": "py3",
                }
            ),
        )
        data = response.get_json()
    assert (
        data["message"]
        == "Wrong values. Programming language not standardized, code is empty or time limit is unreasonable"
    )


def test_judge_end_post_middleware_error_code_empty(app, client) -> None:
    """Test for middleware's empty code judge endpoint."""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                {
                    "code": "",
                    "submission": "19A7B",
                    "input": [1, 2, 3, 4],
                    "output": [1, 4, 9, 16],
                    "time_limit": 1,
                    "memory_limit": 100,
                    "language": "py3",
                }
            ),
        )
        data = response.get_json()
    assert (
        data["message"]
        == "Wrong values. Programming language not standardized, code is empty or time limit is unreasonable"
    )


def test_judge_end_post_middleware_error_not_standardized(app, client) -> None:
    """Test for middleware's not standardized judge endpoint."""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                {
                    "code": "print('Hello World!')\n",
                    "submission": "19A7B",
                    "input": [1, 2, 3, 4],
                    "output": [1, 4, 9, 16],
                    "time_limit": 9,
                    "memory_limit": 100,
                    "language": "pyjava3",
                }
            ),
        )
        data = response.get_json()
    assert (
        data["message"]
        == "Wrong values. Programming language not standardized, code is empty or time limit is unreasonable"
    )


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
