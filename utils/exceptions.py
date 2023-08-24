"""This module contains exceptions classes"""


class RequestFormatError(Exception):
    """
    Exception raised for errors in the format of the incoming request.
    """

    def __init__(self, field_name: str, message: str):
        """Initializes an instance of RequestFormatError
        for errors in request validation.

        Parameters:
        - field_name (str): Name of the field causing the error.
        - message (str): Explanation of the error.
        """
        self.field_name = field_name
        self.message = message
        super().__init__(self.message)
