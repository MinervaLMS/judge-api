""" Endpoint for create problem"""
from typing import Tuple
from flask import Blueprint, jsonify, request, Response
from app.problem.file_creator import FileCreator

problem = Blueprint("problem", __name__)


@problem.route("/problem", methods=["POST"])
def judge_new_problem() -> Tuple[Response, int]:
    """Endpoint for creating and submitting a new problem to the judge.

    Returns:
        A JSON response with a success message and a 200 status code if
        the problem is created successfully.
    """

    data = request.json

    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400

    input_data = data.get("input")
    output_data = data.get("output")
    problem_id = data.get("problem_id")
    points = data.get("points")

    if None in [input_data, output_data, problem_id, points]:
        return jsonify({"error": "Missing required data"}), 400

    problem_creator = FileCreator(problem_id, input_data, output_data, points)

    problem_creator.create_input_output_files()
    problem_creator.create_zip_file()
    problem_creator.create_yaml_file()

    return jsonify({"message": "Problem created successfully."}), 200
