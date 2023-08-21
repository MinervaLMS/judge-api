""" Endpoint for judge's data input """
from flask import Blueprint, json, request
from .endpoint_check import Endpoint_check
from app.executor.executor import Executor


judge_endpoint_bp = Blueprint("judge_endpoint", __name__)


@judge_endpoint_bp.route("/judge/end", methods=["GET", "POST"])
def judge_end() -> (json, int):
    """Endpoint receiving data from back-end
    return: json containing either a error message or the data returned by the executor, and a response status
    """
    check = Endpoint_check(request)

    if not check.judge_data_complete():
        return check.response, 400

    if not check.middleware.validate_code():
        return check.response, 400

    executor = Executor(
        check.middleware.output_data, check.middleware.input_data, check.middleware.code
    )

    return executor.judge(), 201
