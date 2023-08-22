"""This module contains Middleware class"""


class Middleware:
    """
    This class handles code submission validation for the application.
    The Middleware class validates incoming code submissions and ensures
    they meet the necessary criteria.
    """

    def __init__(self, data: dict):
        """
        Initializes an instance of Middleware for request validation.

        Parameters:
        - data (dict):
        A dictionary containing request data to be validated.
        """
        self.code = data["code"]
        self.input = data["input"]
        self.output = data["output"]
        self.time_limit = data["time_limit"]
        self.memory_limit = data["memory_limit"]
        self.language = data["language"]

    def validate_code(self):
        """
        Check if the language name is standardized
        if the code, input and output are not empty
        if the time limit is reasonable
        """
        if not self.standardize_language_name():
            return False

        if not self.empty_data():
            return False

        if self.time_limit > 10000:
            return False

        return True

    def empty_data(self):
        """
        Check if the code, input, output, time_limit,
        memory_limit and language are not empty
        """
        fields_to_check = [
            self.code,
            self.input,
            self.output,
            self.time_limit,
            self.memory_limit,
            self.language,
        ]

        return not any(field == "" for field in fields_to_check)

    def standardize_language_name(self):
        """
        Check if the provided language is supported.
        """
        supported_languages = {
            "python",
            "java",
            "cpp",
        }

        if self.language in supported_languages:
            return True
        return False
