"""Tests for endpoint views."""
from typing import Any
from tests.resources import DATA_ENDPOINT

def test_judge_end_ping(client) -> None:
    """Test for ping endpoint."""
    response = client.get("/ping")
    response.get_data()
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


def test_judge_end_post_failed_missing(app, client, test_power2) -> None:
    """Test for missing JSON keys judge endpoint"""
    
    """Creating the problem."""
    test_power2
    
    with app.app_context():
        response = client.post("/judge/end", json=({"faltan": "valores"}))
        data = response.get_json()
    assert data["message"] == "Missing/wrong key values"


def test_judge_end_IR_verdict(app: Any, client: Any, test_power2) -> None:
    """Test for wrong Json Keys judge endpoint"""
    
    """Creating the problem"""
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    with app.app_context():
        data_end["code"] = "facilito"
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
    data = response.get_json()
    assert data["verdict"]["verdict"] == "IR"


def test_judge_end_post_failed_missing_key(app: Any, client: Any, test_power2) -> None:
    """Test for missing keys at judge endpoint."""
    
    """Creating the problem"""
    test_power2
    
    data_end = DATA_ENDPOINT.copy().pop("language", None)
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing/wrong key values"


def test_judge_end_post_middleware_error_time_limit(app: Any, client: Any, test_power2) -> None:
    data_end=DATA_ENDPOINT.copy()
    data_end["time_limit"] = 10001
    
    "Create problem for this context problem"
    test_power2
    
    with app.app_context():
        """Test for middleware's time limit judge endpoint."""
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Invalid time limit provided."


def test_judge_end_post_middleware_error_code_empty(app: Any, client: Any, test_power2) -> None:
    """Test for middleware's empty code judge endpoint."""
    
    "Create problem for this context problem"
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    data_end["code"] = ""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing or empty code field."


def test_judge_end_post_middleware_error_unsupported_language(app: Any, client: Any, test_power2) -> None:
    """Test for middleware's not standardized judge endpoint."""
    
    "Create problem for this context problem"
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    data_end["language"] = "pyjava3"
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Unsupported language provided."


def test_judge_end_post_middleware_error_empty_problem_id(app: Any, client: Any, test_power2) -> None:
    """Test for middleware's empty input judge endpoint."""
    
    "Create problem for this context problem"
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    data_end["problem_id"] = ""
    with app.app_context():
    
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing or empty problem_id field."


def test_judge_end_post_middleware_error_empty_submission_id(app: Any, client: Any, test_power2) -> None:
    """Test for middleware's not standardized judge endpoint."""
    
    "Create problem for this context problem"
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    data_end["submission_id"] = ""
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(data_end),
        )
        data = response.get_json()
    assert data["message"] == "Missing or empty submission_id field."


def test_judge_end_post_code_test_AC(app, client, test_power2) -> None:
    """Test for executor's accepted code at judge endpoint."""
    
    "Create problem for this context problem"
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                data_end
            ),
        )
        data = response.get_json()
    assert response.status_code == 201 and data["verdict"]["verdict"] == "AC"


def test_judge_end_post_code_test_WA(app, client, test_power2) -> None:
    """Test for executor's wrong answer code at judge endpoint."""
    
    "Create problem for this context problem"
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    with app.app_context():
        data_end["code"]="print(int(input())**2+1)"
        response = client.post(
            "/judge/end",
            json=(
                data_end
            ),
        )
        data = response.get_json()
    assert response.status_code == 201 and data["verdict"]["verdict"] == "WA"
    
def test_judge_end_post_code_test_RTE(app, client, test_power2) -> None:
    """Test for executor's wrong answer code at judge endpoint."""
    
    "Create problem for this context problem"
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    data_end["code"]="import time\ntime.sleep(3)\nprint(int(input())**2+1)"
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                data_end
            ),
        )
        data = response.get_json()
    assert response.status_code == 201 and data["verdict"]["verdict"] == "RTE"
    
def test_judge_end_post_code_test_MLE(app, client, test_power2) -> None:
    """Test for executor's wrong answer code at judge endpoint."""

    "Create problem for this context problem"
    test_power2
    
    data_end=DATA_ENDPOINT.copy()
    data_end["memory_limit"]=1
    with app.app_context():

        response = client.post(
            "/judge/end",
            json=(
                data_end
            ),
        )
        data = response.get_json()
    assert response.status_code == 201 and data["verdict"]["verdict"] == "MLE"
    
def test_judge_end_post_code_test_TLE(app, client, test_power2) -> None:
    """Test for executor's wrong answer code at judge endpoint."""
    data_end=DATA_ENDPOINT.copy()
    
    "Create problem for this context problem"
    test_power2
    
    data_end["code"]="for i in range(0,1000000000):\n\ti+1\nprint(int(input())**2)"
    data_end["time_limit"]=1
    with app.app_context():
        response = client.post(
            "/judge/end",
            json=(
                data_end
            ),
        )
        data = response.get_json()
    assert response.status_code == 201 and data["verdict"]["verdict"] == "TLE"