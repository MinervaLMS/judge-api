"""Here are define pytest fixtures, hooks and plugins. """
from typing import Any
import pytest

from app.DMOJ.judge_connection import SingletonJudge
from tests.resources import DATA_ENDPOINT, DATA_PROBLEM

from app import create_app


@pytest.fixture
def app() -> Any:
    """App fixture."""
    flask_app = create_app()
    return flask_app


@pytest.fixture
def judge_instance():
    """Judge connection"""
    judge = SingletonJudge()
    return judge


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


@pytest.fixture(name="app")
def app_with_create_problem():
    """Fixture providing app for testing problem endpoint"""
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture(name="data_problem")
def data_example():
    """Fixture providing example data for testing new_problem endpoint"""
    return DATA_PROBLEM

@pytest.fixture(name="test_problems_executor")
def test_problems_executor(app,client):
    with app.app_context():
        client.post(
            "/problem",
            json=(
                {
                    "input": ["1"],
                    "output": ["1"],
                    "problem_id": "test_1",
                    "points": [18]
                }
            ),
        )
        client.post(
            "/problem",
            json=(
                {
                    "input": ["1","2","3"],
                    "output": ["1","2","3"],
                    "problem_id": "test_2",
                    "points": [18,36,54]
                }
            ),
        )
        client.post(
            "/problem",
            json=(
                {
                    "input": ["1","10"],
                    "output": ["2","20"],
                    "problem_id": "test_3",
                    "points": [18,36]
                }
            ),
        )
        client.post(
            "/problem",
            json=(
                {
                    "input": ["2","10"],
                    "output": ["[0, 1]","[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"],
                    "problem_id": "test_4",
                    "points": [18,36]
                }
            ),
        )
        client.post(
            "/problem",
            json=(
                {
                    "input": ["2-3"],
                    "output": ["2"],
                    "problem_id": "test_5",
                    "points": [18]
                }
            ),
        )

@pytest.fixture(name="test_power2")
def test_power2(app,client):
    with app.app_context():
        client.post(
            "/problem",
            json=(
                {
                    "input": ["2","3"],
                    "output": ["4","9"],
                    "problem_id": "test_power2",
                    "points": [18,36]
                }
            ),
        )