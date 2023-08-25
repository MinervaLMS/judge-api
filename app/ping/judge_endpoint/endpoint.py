""" Endpoint for judge's data input """
from flask import Blueprint, request, Request
from .endpoint_check import EndpointCheck
from app.executor.executor import Executor


judge_endpoint = Blueprint("judge_endpoint", __name__)


@judge_endpoint.route("/judge/end", methods=["POST"])
def judge_end() -> Request:
    """Endpoint receiving data from back-end

    return: Request containing either a error message or the data returned by the executor.
    """

    check = EndpointCheck(request)
    if not check.judge_data_complete():
        return check.response, 400

    executor = Executor(
        check.middleware.output, check.middleware.input, check.middleware.code
    )

    return executor.judge(), 201
