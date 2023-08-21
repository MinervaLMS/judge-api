"""Code that runs checks in order to confirm data that will be sent to Judge is correct"""

from flask import request, json
from app.middleware.request_validations import Middleware

keys_requested = (
    "code",
    "language",
    "submission",
    "input",
    "output",
    "time_limit",
    "memory_limit",
)


class Endpoint_check:
    def __init__(self, request: request):
        """Class that checks the request received for correction and completeness of judge's input
        Args:
            request: request received from back-end supossedly containing correct data for judge
        Attrs:
            response: dict (Json)
            middleware: Middleware Class"""
        self.request = request
        self.response = None

    def judge_data_complete(self) -> bool:
        """Checks if data needed is fulfilled.
        Archive must be a JSON and contain no more than data in 'keys_requested'"""

        request = self.request
        if request.method == "POST":
            if not request.is_json:
                self.response = {"message": "Not a JSON"}
                return False

            data = request.get_json()
            if (not all(key in keys_requested for key in data)) or len(data) != 7:
                self.response = {"message": "Missing/wrong key values"}
                return False

            self.middleware = Middleware(data)

            if not self.middleware.validate_code():
                self.response = {
                    "message": "Wrong values. Programming language not standardized, code is empty or time limit is unreasonable"
                }
                return False

            return True

        else:
            self.response = {"message": "Not a POST"}
            return False
