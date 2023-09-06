"""Tests for problem endpoint views."""
import json
import os
import zipfile
import yaml
import pytest
from app import create_app
from tests.resources import DATA_PROBLEM
from utils.constants import PROBLEMS_FOLDER


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


def test_judge_new_problem_success(client, data_problem):
    """Test the endpoint for successfully creating a new problem."""
    response = client.post("/problem", json=data_problem)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data["message"] == "Problem created successfully."


def test_create_problem_folder(client, data_problem):
    """Test if the folder problem_id is created successfully."""
    response = client.post("/problem", json=data_problem)
    assert response.status_code == 200

    problem_id = data_problem["problem_id"]
    folder_path = os.path.join(PROBLEMS_FOLDER, problem_id)
    assert os.path.exists(folder_path)


def test_create_yaml_file(client, app, data_problem):
    """Test if the problem_id.yaml file is created successfully."""
    client = app.test_client()

    response = client.post("/problem", json=data_problem)
    assert response.status_code == 200

    problem_id = data_problem["problem_id"]
    yaml_file_path = os.path.join(PROBLEMS_FOLDER, problem_id, "problem.yml")
    assert os.path.exists(yaml_file_path)


def test_create_zip_file(client, app, data_problem):
    """Test if the problem_id.zip file is created successfully."""
    client = app.test_client()

    response = client.post("/problem", json=data_problem)
    assert response.status_code == 200

    problem_id = data_problem["problem_id"]
    zip_file_path = os.path.join(PROBLEMS_FOLDER, problem_id, f"{problem_id}.zip")
    assert os.path.exists(zip_file_path)


def test_zip_content(client, app, data_problem):
    """Test if the contents inside the problem_id.zip file are correct."""
    client = app.test_client()

    response = client.post("/problem", json=data_problem)
    assert response.status_code == 200

    problem_id = data_problem["problem_id"]
    zip_file_path = os.path.join(PROBLEMS_FOLDER, problem_id, f"{problem_id}.zip")
    with zipfile.ZipFile(zip_file_path, "r") as zipf:
        assert f"{problem_id}.1.in" in zipf.namelist()
        assert f"{problem_id}.1.out" in zipf.namelist()
        assert f"{problem_id}.2.in" in zipf.namelist()
        assert f"{problem_id}.2.out" in zipf.namelist()


def test_yaml_content(client, app, data_problem):
    """Test if the contents inside the problem_id.yaml file are correct."""
    client = app.test_client()

    response = client.post("/problem", json=data_problem)
    assert response.status_code == 200

    problem_id = data_problem["problem_id"]
    yaml_file_path = os.path.join(PROBLEMS_FOLDER, problem_id, "problem.yml")
    with open(yaml_file_path, "r", encoding="utf-8") as yml_file:
        yml_data = yaml.safe_load(yml_file)
        assert "archive" in yml_data
        assert "test_cases" in yml_data
        assert {
            "in": "EDM05E01.1.in",
            "out": "EDM05E01.1.out",
            "points": 45,
        } in yml_data["test_cases"]
