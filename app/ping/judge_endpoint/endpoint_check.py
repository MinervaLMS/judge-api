"""Code that runs checks in order to confirm data that will be sent to Judge is correct"""

from flask import request, Request
from app.middleware.request_validations import Middleware
from app.utils.constants import KEYS_REQUESTED


class EndpointCheck:
    def __init__(self, request: Request):
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
        Request must contain a dict (Json) with no more and no less than data in 'KEYS_REQUESTED'

            Returns:
                    Bool. True if request is correct and complete, False otherwise.
        """

        request = self.request

        if not request.is_json:
            self.response = {"message": "Not a JSON"}
            return False

        data = request.get_json()
        if (not all(key in KEYS_REQUESTED for key in data)) or len(data) != 7:
            self.response = {"message": "Missing/wrong key values"}
            return False

        self.middleware = Middleware(data)
        self.response = {"message" : self.middleware.validate_code()}

        if self.response["message"] != "Valid submission":
            return False

        return True
