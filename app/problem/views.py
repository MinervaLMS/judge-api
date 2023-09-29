""" Endpoint for create problem"""
from typing import Tuple
from flask import Blueprint, jsonify, request, Response
from app.problem.file_creator import FileCreator

problem = Blueprint("problem", __name__)


@problem.route("/problem", methods=["POST"])
def new_problem() -> Tuple[Response, int]:
    """Endpoint for creating and submitting a new problem to the judge.

    Returns:
        A JSON response with a success message and a 200 status code if
        the problem is created successfully.
    """

    data = request.json

    problem_creator = FileCreator(
        data.get("problem_id"),
        data.get("input"),
        data.get("output"),
        data.get("points"),
    )
    problem_creator.save()

    return jsonify({"message": "Problem created successfully."}), 200